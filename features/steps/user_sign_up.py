from behave import *
import re

@given("at the Sign-Up page")
def step_impl(context):
    context.browser.get(context.address + "/showSignUp")
    signUp_found = re.search("signUp", context.browser.page_source, re.IGNORECASE)
    assert signUp_found

@when("the {inputName} or {inputEmail} is already exist. it does not matter if {inputPassword} is exist or not.")
def step_impl(context, inputName, inputEmail, inputPassword):
    """
    :type context: behave.runner.Context
    :type inputName: str
    :type inputEmail: str
    :type inputPassword: str
    """
    submit_inputName_inputEmail(context, inputName, inputEmail, inputPassword)

@when("the {inputName} or {inputEmail} is not exist in db. it does not matter if {inputPassword} is exist or not.")
def step_impl(context, inputName, inputEmail, inputPassword):
    """
    :type context: behave.runner.Context
    :type inputName: str
    :type inputEmail: str
	:type inputPassword: str
    """
    submit_inputName_inputEmail(context, inputName, inputEmail, inputPassword)

def submit_inputName_inputEmail(context, inputName, inputEmail, inputPassword):
    inputName_field = context.browser.find_element_by_name("inputName")
    inputEmail_field = context.browser.find_element_by_name("inputEmail")
    inputPassword_field = context.browser.find_element_by_name("inputPassword")
    inputName_field.send_keys(inputName)
    inputEmail_field.send_keys(inputEmail)
    inputPassword_field.send_keys(inputPassword)
    inputName_field.submit()
    context.response = context.browser.page_source


@then('the system should return "{text}" as the registration status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
  
