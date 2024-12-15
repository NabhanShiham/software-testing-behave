from behave import *
from hamcrest import assert_that, equal_to
import time


@given("the '{sns}' link is clicked")
def step_impl(context, sns):
    context.homepage.click_social_network_button(sns)
    time.sleep(5)


@then("the correct '{webpage}' is displayed")
def step_impl(context, webpage):
    expected_url = webpage
    context.homepage.driver.switch_to.window(context.homepage.driver.window_handles[1])
    current_url = context.homepage.get_current_url()
    assert_that(current_url, equal_to(expected_url))
    context.homepage.driver.close()
    context.homepage.driver.switch_to.window(context.homepage.driver.window_handles[0])

