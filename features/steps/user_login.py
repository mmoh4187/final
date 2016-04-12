from behave import *
import re

@given("at the login screen")
def step_impl(context):
    context.browser.get(context.address + "/showSignIn")
    validateLogin_found = re.search("validateLogin", context.browser.page_source, re.IGNORECASE)
    assert validateLogin_found

@when("an existing user submits the correct {InputUsername} and {inputPassword}")
def step_impl(context, InputUsername, inputPassword):
    """
    :type context: behave.runner.Context
    :type InputUsername: str
    :type inputPassword: str
    """
    submit_InputUsername_inputPassword(context, InputUsername, inputPassword)

@when("an existing user submits the correct {InputUsername} but incorrect {inputPassword}")
def step_impl(context, InputUsername, inputPassword):
    """
    :type context: behave.runner.Context
    :type InputUsername: str
    :type inputPassword: str
    """
    submit_InputUsername_inputPassword(context, InputUsername, inputPassword)


@when("an unknown user submits some {InputUsername} and {inputPassword}")
def step_impl(context, InputUsername, inputPassword):
    """
    :type context: behave.runner.Context
    :type InputUsername: str
    :type inputPassword: str
    """
    submit_InputUsername_inputPassword(context, InputUsername, inputPassword)
def submit_InputUsername_inputPassword(context, InputUsername, inputPassword):
    InputUsername_field = context.browser.find_element_by_name("InputUsername")
    inputPassword_field = context.browser.find_element_by_name("inputPassword")
    InputUsername_field.send_keys(InputUsername)
    inputPassword_field.send_keys(inputPassword)
    InputUsername_field.submit()
    context.response = context.browser.page_source


@then('the system should return "{text}" as the authentication status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
   
