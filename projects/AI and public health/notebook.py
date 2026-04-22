import asyncio
import datetime
import hashlib
from playwright.async_api import async_playwright

async def run_sentinel_connect(url, brand_name):
    async with async_playwright() as p:
        # Connect to the REAL browser you opened in Step 1
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        
        # Access the already-open context
        context = browser.contexts[0]
        page = await context.new_page()
        
        print(f"Agent connected to live browser. Navigating to {brand_name}...")
        
        # Navigate
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(5000) # Wait for videos to pop up

        # Capture Evidence
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sentinel_capture_{brand_name}_{timestamp}.png"
        await page.screenshot(path=filename, full_page=True)
        
        # Forensic Fingerprint
        with open(filename, "rb") as f:
            fingerprint = hashlib.sha256(f.read()).hexdigest()

        print(f"\n--- MISSION SUCCESS ---")
        print(f"Evidence Secured: {filename}")
        print(f"Forensic Hash: {fingerprint}")

if __name__ == "__main__":
    target_url = "https://www.youtube.com/@Coca-Cola/videos"
    asyncio.run(run_sentinel_connect(target_url, "Coca-Cola"))