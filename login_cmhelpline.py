from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    # Check if state.json exists
    if not os.path.exists("state_CM.json"):
        print("Error: state.json not found!")
        print("Please run storage_state_cmhelpline.py first to create the session")
        browser.close()
        exit()
    
    try:
        print("=" * 60)
        print("LOADING SAVED SESSION FROM state.json")
        print("=" * 60)
        
        # Use saved session with custom User-Agent
        print("\n1. Creating context with saved session and custom User-Agent...")
        context = browser.new_context(
            storage_state="state_CM.json",
            #user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        print("   ✓ Session loaded with custom User-Agent")
        
        # Navigate to dashboard
        print("\n2. Opening dashboard...")
        page.goto('https://cmhelpline.mp.gov.in/MIS/dashboard.aspx', timeout=30000)
        page.wait_for_load_state('networkidle', timeout=15000)
        print("   ✓ Dashboard opened successfully")
        
        current_url = page.url
        print(f"\n3. Current URL: {current_url}")
        
        # Take screenshot
        page.screenshot(path='dashboard_screenshot.png')
        print("   ✓ Screenshot saved: dashboard_screenshot.png")
        
        print("\n" + "=" * 60)
        print("SESSION ACTIVE - DASHBOARD LOADED")
        print("=" * 60)
        
        # Keep page open
        page.wait_for_timeout(10000)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nPossible reasons:")
        print("1. Session expired - run storage_state_cmhelpline.py again")
        print("2. Website server error")
        print("3. Network connectivity issue")
        
        try:
            page.screenshot(path='error_screenshot.png')
            print("\nScreenshot saved: error_screenshot.png")
        except:
            pass
            
    finally:
        browser.close()