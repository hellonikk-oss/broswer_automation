from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
  
    
    page=browser.new_page()
    page.goto('https://www.screener.in/login/')
    print('open')
    
    
    #xpath using text
   
    username= page.wait_for_selector('//input[@id="id_username"]')
    username.fill('slrdamoh@gmail.com')
    password= page.wait_for_selector('//input[@id="id_password"]')
    password.fill('arybhatt06')
    page.wait_for_timeout(10000)
    button= page.wait_for_selector('//button[@type="submit"]')
    button.click()
    page.wait_for_timeout(5000)
    print ('successfully login  ')
    browser.close()
    # xpath using attribute
    # username= page.wait_for_selector('//input[@name="username"]')
    # username.type('Admin')      
    # password= page.wait_for_selector('//input[@placeholder="Password"]')
    # password.type('admin123')
    # page.wait_for_timeout(10000)
    # button= page.wait_for_selector('//button[@type="submit"]')
    # button.click()
    # page.wait_for_timeout(10000)
    # browser.close()
    # print('successfully login  ')
    
    
    # # css selector id
    # page.wait_for_selector('#email')
    # page.fill('#email', 'test@example.com')
    # page.wait_for_selector('#enterimg')
    # page.wait_for_timeout(10000)
    # page.click('#enterimg')
    # page.wait_for_timeout(10000)
    # browser.close()
    
    #css selector attribute
    # username= page.locator('input[name="username"]')
    # username.type('Admin')      
    # password= page.locator('input[type="password"]')
    # password.type('admin123')
    # page.wait_for_timeout(10000)
    # button= page.locator('button[type="submit"]')
    # button.click()
    # page.wait_for_timeout(10000)
    # browser.close()
    # print('successfully login  ')
    
    # #table
    # table= page.locator('//table[@id="example"]')
    # rows= table.locator('tr')
    
    # columns= table.locator('th') #for header columns
    # #second row text
    # second_row= rows.nth(1)
    # second_row_cells= second_row.locator('td')
    
    # #or selectind cell\
    # cell = page.locator('//*[@id="example"]//tbody//tr//td[contains(text(), 'कामनी')]')
    # #or 
    # cell_1  = page.locator('//*[@id="example"]/tbody/tr[5]/td[5]')
    
    
    # second_row_text= second_row_cells.all_inner_texts()
    # print(second_row_text)
    
    # #read all rows and columns

    # table= page.locator('//table[@id="example"]')
    # rows= table.locator('tr')
    # all_rows_data=rows.all()
    # for row in all_rows_data:
    #     cells=row.locator('td')
    #     row_data=cells.all_inner_texts()
    #     print(row_data)
    
   