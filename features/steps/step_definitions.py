from behave import given, then

from resources.config import Config
from pages.base_page import DriverManager
from pages.landing_page import HomePage


@given('I am on the Elucidat learning platform')
def step_impl(context):
    context.driver = DriverManager.launch_browser_and_navigate(Config.BASE_URL)

@then('I verify the title is "{title}"')
def step_impl(context, title):
    home_page = HomePage(context.driver)
    assert home_page.get_title() == title

@then('I click on the START button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_start_button()


@then('I click on the Making a case against Kevin')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_case_against_kavin_button()
    
    
@then('I click on JUDGE THIS button')
def step_then_i_click_judge_this(context):
    home_page = HomePage(context.driver)
    home_page.click_judge_this()

@then('I click on Guilty Radio')
def step_then_i_click_guilty_radio(context):
    home_page = HomePage(context.driver)
    home_page.click_guilty_radio()

@then('I click on Vote button')
def step_then_i_click_vote_button(context):
    home_page = HomePage(context.driver)
    home_page.click_vote_button()

@then('I verify NOT GUILTY! headings on pop-up')
def step_then_i_verify_not_guilty(context):
    home_page = HomePage(context.driver)
    assert home_page.verify_not_guilty()


@then('I click on the continue button on NOT GUILTY! pop-up')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_continue_button_1()

@then('I click on the continue button on Our expert agrees pop-up')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_continue_button_on_our_expert_agree()

@then('I click on the continue button on EXPLORE THE EVIDENCE page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_continue_button_2()


# @then('I click on the continue button_2')
# def step_impl(context):
#     home_page = HomePage(context.driver)
#     home_page.click_continue_button_1()

@then('I click on continue button 2')
def step_then_i_click_continue_button_2(context):
    home_page = HomePage(context.driver)
    home_page.click_continue_button_2()

@then('I verify YOU DECIDE headings')
def step_then_i_verify_you_decide(context):
    home_page = HomePage(context.driver)
    assert home_page.verify_you_decide()

@then('I click on continue button on YOU DECIDE page')
def step_then_i_click_continue_button_3(context):
    home_page = HomePage(context.driver)
    home_page.click_continue_button_2()  # Reusing the same method as the XPath is the same

@then('I click on flip button')
def step_then_i_click_flip_button(context):
    home_page = HomePage(context.driver)
    home_page.click_flip_button()

@then('I click on Can be reliable radio button')
def step_then_i_click_can_be_reliable_radio(context):
    home_page = HomePage(context.driver)
    home_page.click_can_be_reliable_radio()

@then('I click on Vote button again')
def step_then_i_click_vote_button_again(context):
    home_page = HomePage(context.driver)
    home_page.click_vote_button()

@then('I verify Our expert agrees headings on pop-up')
def step_then_i_verify_our_expert_agrees(context):
    home_page = HomePage(context.driver)
    assert home_page.verify_our_expert_agrees()