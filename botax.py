import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://faucet.botanixlabs.dev/"  # Replace with actual faucet URL if different
BOTANIX_TESTNET_ADDRESS = "your-evm-wallet-address-here"  # Replace with your Botanix testnet wallet address

async def claim_botanix_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set True to run headless
        page = await browser.new_page()

        # Navigate to faucet page
        await page.goto(FAUCET_URL)

        # Wait for wallet address input box - adjust selector if needed
        await page.wait_for_selector('input[type="text"], input[placeholder*="address"]')

        # Fill in your testnet wallet address
        await page.fill('input[type="text"], input[placeholder*="address"]', BOTANIX_TESTNET_ADDRESS)

        # Click the "Get" or "Claim" button - adjust selector to actual button text or class
        await page.click('button:has-text("Get"), button:has-text("Claim")')

        # Wait for confirmation message or timeout
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No success confirmation detected. Please check manually.")

        # Close browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_botanix_faucet())
