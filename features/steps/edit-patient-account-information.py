from behave import *
import os
from source.database import Database
from source.patient import Patient

use_step_matcher("re")


@given("As doctor i want to edit the patient's account information")
def step_impl(context):
    root_dir = os.getcwd()
    database = Database(root_dir)
    database.load_database()
    context.patients_accounts = database.patients_accounts


@when(
    "I input (?P<national_code>.+), (?P<name>.+), (?P<lastname>.+), (?P<birthdate>.+), (?P<father_name>.+) of patinet")
def step_impl(context, national_code, name, lastname, birthdate, father_name):
    patient_object = Patient(context.patients_accounts)
    context.return_value = patient_object.edit_patient_account(national_code, name, lastname, birthdate, father_name)


@then("the result of edition will be (?P<return_value>.+)")
def step_impl(context, return_value):
    assert context.return_value == eval(return_value)
