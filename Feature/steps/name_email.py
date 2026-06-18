from behave import when
from selenium.webdriver.common.by import By

from Feature.pom.address import name_email


@when('enter {name} and {email}')
def fill_name_email(context, name, email):
    name_email_page = name_email(context.driver)
    name_email_page.enter_name_email(name, email)