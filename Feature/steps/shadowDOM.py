from behave import when
from selenium.webdriver.common.by import By


@when('get shadow DOM object')
def get_shadow_dom_object(context):
    shadow_host = context.driver.find_element(By.ID, "shadow_host")
    shadow_root = context.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    textbox = shadow_root.find_element(By.CSS_SELECTOR, "input[type='text']")
    textbox.send_keys("Hello Shadow DOM!")
