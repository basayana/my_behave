from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
import os
import allure

def before_scenario(context, scenario):
    # Ensure the screenshots directory exists
    os.makedirs("screenshots", exist_ok=True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://testautomationpractice.blogspot.com/")

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
