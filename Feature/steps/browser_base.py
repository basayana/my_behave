import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import given, when, then

from webdriver_manager.chrome import ChromeDriverManager
@given('open browser with URL {url}')
def open_browser(context, url):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print(f'URL_is: {url}')
    context.driver.get(url)
    # print(f'PAGECONTENT_START:{context.driver.page_source}')
    print('END_OF_PAGECONTENT')
    context.driver.maximize_window()
    time.sleep(3)

@then('close browser')
def close_browser(context):
    time.sleep(5)
    context.driver.quit()