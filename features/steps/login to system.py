from behave import *
import os
from source.login import Login
from source.database import Database


use_step_matcher("re")


@given("sign in doctor to system")
def step_impl(context):
    pass


@when("As a doctor, I have to enter my (?P<username>.+) and (?P<password>.+)\.")
def step_impl(context, username, password):
    current_directory = os.getcwd()
    database_object = Database(current_directory)
    database_object.load_database()
    login_object = Login(database_object)
    login_object.log_in(username, password)
    context.login_result = login_object.log_validation


@then("The return value of my login process to system will be (?P<validation>.+)\.")
def step_impl(context, validation):
    assert context.login_result == eval(validation)