from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()    
    page=browser.new_page()
    page.goto('https://www.screener.in/login/')
    print('open')
    

   
    username= page.wait_for_selector('//input[@id="id_username"]')
    username.fill('slrdamoh@gmail.com')
    password= page.wait_for_selector('//input[@id="id_password"]')
    password.fill('arybhatt06')
    page.wait_for_timeout(1000)
    button= page.wait_for_selector('//button[@type="submit"]')
    button.click()
    page.wait_for_timeout(1000)
    print ('successfully login  ')
    context.storage_state(path='state_scr.json')
    
    browser.close()