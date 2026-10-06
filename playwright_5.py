from playwright.sync_api import sync_playwright

#function for 
def download_handle(download):
    print('download started')
    download.save_as('./files/girdavari_status_1.xls')  # provide the path where you want to save the downloaded file
    print('download completed')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    
    #upload file
    # page.goto('https://demo.automationtesting.in/FileUpload.html')
    # print('open')
    # file_upload = './imdb.xlsx '  
    # upload_location = page.query_selector('//input[@id="input-4"]')
    # upload_location.set_input_files(file_upload)
    # page.wait_for_timeout(5000)
    # print('file uploaded')
    
    #download file
    page.goto('https://saara.mp.gov.in/saaraweb/PublicReport/frm_PerWiseGirdavariStatus.aspx ') # plz provide  the url for download file
    print('open')
    page.wait_for_selector("//a[@id='ContentPlaceHolder1_grdDistrictWise_lnkViewDetails_32']").click()
    page.on('download', download_handle)#
    page.wait_for_selector('//input[@id="ContentPlaceHolder1_lnk_Export_Tehsil"]').click()
    
    page.wait_for_timeout(5000)
    browser.close() 