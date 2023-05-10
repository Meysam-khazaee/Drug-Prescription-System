import pytest
import os
from pytest import MonkeyPatch
from source.visit import Visit
from source.database import Database

@pytest.fixture(scope='session')
def setup():
    os.chdir('..')
    root_dir = os.getcwd()
    database = Database(root_dir)
    database.load_database()
    return database


@pytest.fixture(scope='session')
def teardown():
    pass


class TestPatient(object):

    def test_report(self):
        assert False

    visit_previous_prescriptions_test_data = [
        (["3860960903"], ["1", "3", "y"], "Ozempic,3.0,1,10\n"),
        (["3860960903"], ["4", "4", "y"], "Ativan,4.0,1,10\n"),
        (["4960011100"], ["2", "2", "y"], "Entresto,2.0,1,10\n")
    ]

    @pytest.mark.parametrize("input_code,test_input,expected", visit_previous_prescriptions_test_data)
    def test_previous_prescriptions(self, setup, teardown, input_code, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        patient_medicine_list = []
        visit_object = Visit(database.patients_accounts, database.medicines_list, patient_medicine_list)
        previous_prescriptions_result = visit_object.previous_prescriptions(input_code[0])
        assert previous_prescriptions_result == expected


    def test_prescribe_from_medicines_list(self):
        assert False
