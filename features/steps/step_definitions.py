from behave import given

from resources.config import Config
from pages.base_page import BasePage


@given('I am on the Elucidat learning platform')
def step_impl(context):
    context.driver = BasePage.launch_browser_and_navigate(Config.BASE_URL)