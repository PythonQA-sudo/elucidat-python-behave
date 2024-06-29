from behave import given, then

from features.resources.config import Config
from features.pages.base_page import BasePage
from features.pages.landing_page import HomePage

@given('I am on the Elucidat learning platform')
def step_impl(context):
    context.driver = BasePage.launch_browser_and_navigate(Config.BASE_URL)