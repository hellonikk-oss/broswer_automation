from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    print('open')
    #provided by ai
    with context.expect_page() as new_page_info:
        page.wait_for_selector('//button[text()="    click   "]').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()

    total_page = context.pages
    print(len(total_page))
    for i in total_page:
        print(i.url)

    print(page.title())
    new_page.bring_to_front()
    page.wait_for_timeout(5000)
    print(new_page.title())
    new_page.close()
    page.wait_for_timeout(5000)

    browser.close()