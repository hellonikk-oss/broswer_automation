from playwright.sync_api import expect, sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    #locating table method 1
    page.goto('https://testautomationpractice.blogspot.com/')
    table = page.locator("//table[@name='BookTable']") #locating table method 1
    expect(table).to_be_visible()
    #row selector
    rows = table.locator('tr')
    expect(rows).to_have_count(7)
    print(f"Number of rows in table: {rows.count()}")
    page.wait_for_timeout(5000)
   # print(table.inner_text())
   #column selector
    columns = rows.locator('th')
    print(f"Number of columns in table: {columns.count()}")
    page.wait_for_timeout(5000)

    #reading data from second row
    # second_row_cells = rows.nth(1).locator('td')
    # second_row_text = second_row_cells.all_inner_texts()
    # print(f"Text in second row=======>: {second_row_text}")
    # for i in second_row_text:
    #     print(i)
    
    #read all the date from table (except header)
    all_row_data = rows.all()   
    
    for row in all_row_data[1:]:  # Skip the header row
        cells = row.locator('td')
        cell_texts = cells.all_inner_texts()
        print(f"Text in row: {cell_texts}")

    #print book name whose author is Mukesh
    # for row in all_row_data[1:]:  # Skip the header row
    #     cells = row.locator('td').nth(1)  # Author column
    #     auth_name = cells.all_inner_texts()
    #     print(f"author name: {auth_name}")
    #     if "Mukesh" in auth_name:
    #         book_name = row.locator('td').nth(0).inner_text()  # Book Name column
    #         print(f"Book name whose author is Mukesh: {book_name}")

    browser.close() 
    
    