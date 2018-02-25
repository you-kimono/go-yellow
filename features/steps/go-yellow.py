from behave import *
from selenium import webdriver

@given('no preconditions')
def step_impl(context):
    pass

@when('we open the homepage')
def step_impl(context):
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')

@then('the title contains \'go-yellow\'')
def step_impl(context):
    assert 'go-yellow' in browser.title
