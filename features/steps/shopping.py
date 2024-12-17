from behave import *
from hamcrest import assert_that, equal_to


@then("the price should read '{total}'")
def step_impl(context, total):
    assert_that(context.homepage.total(), equal_to(total))


@step("the checkout information is missing the '{field}'")
def step_impl(context, field):
    if field == 'First Name':
        context.homepage.fill_out_field('Last Name', 'test_last')
        context.homepage.fill_out_field('Zip Code', '2003')

    if field == 'Last Name':
        context.homepage.fill_out_field('First Name', 'test_first')
        context.homepage.fill_out_field('Zip Code', '2003')

    if field == 'Zip Code':
        context.homepage.fill_out_field('First Name', 'test_first')
        context.homepage.fill_out_field('Last Name', 'test_last')


@then("the '{checkoutError}' is shown")
def step_impl(context, checkoutError):
    assert_that(context.homepage.get_checkout_error(), equal_to(checkoutError))
