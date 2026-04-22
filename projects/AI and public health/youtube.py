import asyncio
import datetime
import hashlib
from playwright.async_api import async_playwright

async def run_youtube_sentinel(channel_url, brand_name):
    async with async_playwright() as p:
        # 1. Launch visible browser to avoid 'Page Not Available' errors
        browser = await p.chromium.launch(headless=False)
        
        # 2. Set a real-user identity
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        print(f"Opening YouTube for {brand_name}...")
        
        # 3. Go to the URL
        await page.goto(channel_url, wait_until="networkidle")

        # 4. Give the thumbnails 10 seconds to load fully
        print("Waiting for content to render...")
        await page.wait_for_timeout(10000) 

        # 5. Capture & Hash
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"youtube_evidence_{brand_name}_{timestamp}.png"
        await page.screenshot(path=filename, full_page=True)
        
        with open(filename, "rb") as f:
            fingerprint = hashlib.sha256(f.read()).hexdigest()
        
        print(f"\n--- SUCCESS ---")
        print(f"Evidence Saved: {filename}")
        print(f"Forensic Hash: {fingerprint}")
        
        await browser.close()

if __name__ == "__main__":
    # Ensure the URL is exactly correct
    target = "https://www.youtube.com/@cocacola/videos"
    asyncio.run(run_youtube_sentinel(target, "Coca-Cola"))