from behave import when
from selenium.webdriver.common.by import By

from Features.pom.address import name_email
import logging

logger = logging.getLogger(__name__)

@when('enter {name} and {email}')
def fill_name_email(context, name, email):
    name_email_page = name_email(context.driver)
    name_email_page.enter_name_email(name, email)
    print(f"%%%%%%%%%%%%%Entered name: {name}, email: {email}", flush=True)
    logger.info(f"******************")
    assert 1==1