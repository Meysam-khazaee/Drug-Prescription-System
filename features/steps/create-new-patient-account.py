from behave import *
import os
from source.patient import Patient
from source.database import Database

use_step_matcher("re")


@given("As doctor i want create patient account")
def step_impl(context):
    root_dir = os.getcwd()
    database = Database(root_dir)
    database.load_database()
    context.database = database


@when("I entered (?P<name>.+), (?P<lastname>.+), (?P<national_code>.+), (?P<birth_date>.+), (?P<father_name>.+)")
def step_impl(context, name, lastname, national_code, birth_date, father_name):
    patient_object = Patient(context.database.patients_accounts)
    context.return_value = patient_object.create_new_patient_account(name, lastname, national_code, birth_date, father_name)


@then("the result of new account creation will be (?P<return_value>.+)")
def step_impl(context, return_value):
    assert context.return_value == eval(return_value)

