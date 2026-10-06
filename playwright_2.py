from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    print('open')
    
#dropdown selection method  1
    dropdown_1 = page.wait_for_selector('//select[@id="Skills"]')
    dropdown_1.select_option('Android')
    page.wait_for_timeout(3000)
    print('successfully select dropdown value')
    #dropdown selection method  
    # page.select_option('//select[@id="Skills"]', 'Android')
    # page.wait_for_timeout(5000)
    if dropdown_1.input_value() == 'Android':
        print('dropdown value is selected')
    else:
        print('dropdown value is not selected')
    
    
    
    # radio button selection
    radio_1 = page.wait_for_selector('//input[@value="FeMale"]')
    radio_1.check()
    page.wait_for_timeout(3000)
    print('successfully select radio button')
    if radio_1.is_checked():
        print('radio button is selected')  
    else:
        print('radio button is not selected')        
        
        
    #checkbox selection
    checkbox_1 = page.wait_for_selector('//input[@value ="Cricket"]')
    checkbox_1.check()
    page.wait_for_timeout(3000)
    print('successfully select checkbox')
    
    if checkbox_1.is_checked():
        print('checkbox is selected')
    else:
         print('checkbox is not selected')
    
    
    
    browser.close()