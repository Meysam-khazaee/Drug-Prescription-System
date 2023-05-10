from behave import *
import os
from source.database import Database
from source.patient import Patient

use_step_matcher("re")


@given("As doctor i want to delete patient's account")
def step_impl(context):
    root_dir = os.getcwd()
    database = Database(root_dir)
    database.load_database()
    context.patients_accounts = database.patients_accounts


@when("I input the (?P<national_code>.+) of patient as national code")
def step_impl(context, national_code):
    patient_object = Patient(context.patients_accounts)
    context.return_value = patient_object.delete_patient_account(national_code)


@then("the result of delete process will be (?P<return_value>.+)")
def step_impl(context, return_value):
    assert context.return_value == eval(return_value)