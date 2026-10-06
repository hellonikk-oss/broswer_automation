from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    print('open')
    #Alert with OK
    # page.wait_for_selector('//div[@id="OKTab"]/button').click
    # page.wait_for_timeout(3000)
    # print('successfully click on alert with ok button')
    # page.wait_for_timeout(3000)
    
    #Alert with OK & Cancel
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.on('dialog', lambda dialog: dialog.accept())
    #page.on('dialog', lambda dialog: dialog.dismiss())
    page.on('dialog', lambda dialog: print(dialog.message))
    page.wait_for_selector("//button[@class='btn btn-primary']").click()
    print('successfully click on alert with ok and cancel button')
    page.wait_for_timeout(5000)
    
    
    
    browser.close()