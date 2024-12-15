from behave import *
from hamcrest import assert_that, equal_to


@then("the price should read '{total}'")
def step_impl(context, total):
    assert_that(context.homepage.total(), equal_to(total))


