from playwright.sync_api import sync_playwright
import os

from requests import delete
state_file = 'state_SCR.json'
if os.path.exists(state_file):
    os.remove(state_file)
    
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("Opening login page...")
        page.goto('https://www.screener.in/login/', timeout=30000)
        #page.wait_for_load_state('networkidle')
        print("Login page opened.")

        # Enter username
        username= page.wait_for_selector('//input[@id="id_username"]')
        username.fill('slrdamoh@gmail.com')
        password= page.wait_for_selector('//input[@id="id_password"]')
        password.fill('arybhatt06')
        page.wait_for_timeout(1000)
        
                
        # Click submit button
        try:
            button= page.wait_for_selector('//button[@type="submit"]')
            button.click()
            print("Login button clicked.")
        except Exception as e:
            print("Login button not found. Error:", e)
            raise

        # Wait for successful login
        #page.wait_for_load_state('networkidle', timeout=15000)
        print("Login successful.")

        # Save session state
        context.storage_state(path='state_SCR.json')
        print("Session state saved to state_SCR.json.")

    except Exception as e:
        print("An error occurred:", e)
        page.screenshot(path='error_screenshot.png')
        print("Screenshot saved as error_screenshot.png for debugging.")

    finally:
        browser.close()