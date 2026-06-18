# test_connection.py  — run this first
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
driver.get("https://www.google.com")
print("✅ Title:", driver.title)
driver.quit()