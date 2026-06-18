from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
import allure

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

HUB_URL = os.getenv("SELENIUM_HUB_URL", "http://localhost:4444/wd/hub")
BROWSER = os.getenv("BROWSER", "chromium").lower()

def before_feature(context, feature):
    os.makedirs("screenshots", exist_ok=True)

    if BROWSER in ("chromium", "chrome"):
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        context.driver = webdriver.Remote(
            command_executor=HUB_URL,
            options=options
        )
    elif BROWSER == "firefox":
        options = FirefoxOptions()
        context.driver = webdriver.Remote(
            command_executor=HUB_URL,
            options=options
        )

    context.driver.implicitly_wait(10)
    context.driver.get("https://testautomationpractice.blogspot.com/")

def after_feature(context, feature):
    if hasattr(context, "driver"):
        context.driver.quit()

def after_scenario(context, scenario):
    driver = getattr(context, "driver", None)
    if scenario.status in ("failed", "error"):
        if isinstance(driver, WebDriver):
            try:
                os.makedirs("screenshots", exist_ok=True)
                scenario_name = scenario.name.replace(" ", "_")
                filename = f"screenshots/{scenario_name}_after_scenario.png"
                driver.save_screenshot(filename)
                print(f"[AFTER_SCENARIO] Screenshot saved to {filename}", flush=True)
                # Attach screenshot to Allure report
                with open(filename, "rb") as image_file:
                    allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"[AFTER_SCENARIO][ERROR] Failed to save screenshot: {e}", flush=True)
        else:
            print("[AFTER_SCENARIO][ERROR] context.driver is not a valid WebDriver instance.", flush=True)
