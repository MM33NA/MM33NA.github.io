import asyncio
import os
import datetime
import hashlib
from playwright.async_api import async_playwright

async def run_sentinel_agent(url, brand_name):
    async with async_playwright() as p:
        # We launch a normal browser without the 'Robot' flags
        browser = await p.chromium.launch(headless=False)
        
        # We create a context that DOES NOT save to a folder (to clear the 'Incorrect' error)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        
        print(f"Opening {url}...")
        await page.goto(url, wait_until="networkidle")

        # 1. THE GATEWAY BRIDGE
        print("\n--- ACTION REQUIRED ---")
        print("Please log in manually. If you see 'Incorrect Password', click 'Forgot Password'")
        print("and reset it right here in this window. I will wait for you.")
        
        # We wait for 3 minutes (180s) to give you time to reset the password if needed
        await page.wait_for_timeout(180000) 

        # 2. THE CAPTURE (Only runs after your 3 minutes are up)
        print("Time is up! Capturing current view...")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"evidence_{brand_name}_{timestamp}.png"
        await page.screenshot(path=filename, full_page=True)
        
        # 3. THE FINGERPRINT
        with open(filename, "rb") as f:
            fingerprint = hashlib.sha256(f.read()).hexdigest()

        print(f"\n--- SUCCESS ---")
        print(f"Evidence Saved: {filename}")
        print(f"Fingerprint: {fingerprint}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_sentinel_agent("https://www.instagram.com/cocacola/", "Coca-Cola"))