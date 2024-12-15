from behave import *
from hamcrest import assert_that, equal_to


@given("the '{product}' is added to the cart")
def step_impl(context, product):
    context.homepage.add_to_cart(product)


@then("the cart does not contain anything")
def step_impl(context):
    assert_that(context.homepage.cart_is_empty(), equal_to(True))


@when("the '{product}' is removed from the cart")
def step_impl(context, product):
    context.homepage.remove_from_cart(product)


@then("the cart should contain 2 products")
def step_impl(context):
    assert_that(context.homepage.cart_contains(), equal_to(2))


@then("the cart should contain 3 products")
def step_impl(context):
    assert_that(context.homepage.cart_contains(), equal_to(3))


@step("the '{product}' is removed from the cart")
def step_impl(context, product):
    context.homepage.remove_from_cart(product)


@given("everything is added to the cart")
def step_impl(context):
    for product in context.homepage.item_buttons:
        context.homepage.add_to_cart(product)
