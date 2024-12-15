from behave import *
from hamcrest import assert_that, equal_to


@given("the filter is set to '{filter_by}'")
def step_impl(context, filter_by):
    context.homepage.select_filter(filter_by)


@then("the first product should be '{product}'")
def step_impl(context, product):
    assert_that(context.homepage.get_first_product(), equal_to(product))
