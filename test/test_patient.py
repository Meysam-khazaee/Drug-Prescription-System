import pytest
import os
from pytest import MonkeyPatch
from source.patient import Patient
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
    search_patient_account_test_data = [
        (["4960011100"], True),
        (["3860601325"], True),
        (["4969053625"], True),
        (["3860605783"], True),
        (["4969604963"], True),
        (["3872052053"], True),
        (["3363363333"], False),
        (["3360274210"], False)
    ]

    @pytest.mark.parametrize("test_input,expected", search_patient_account_test_data)
    def test_search_patient_account(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        patient_object = Patient(database.patients_accounts)
        search_result = patient_object.search_patient_account(test_input[0])
        assert search_result == expected

    test_delete_patient_account_test_data = [
        (["3860601325"], True),
        (["4969053625"], True),
        (["3860605783"], True),
        (["4969604963"], True),
        (["3872052053"], True),
        (["3360274210"], False),
        (["3363363332"], False),
        (["3360274211"], False)
    ]

    @pytest.mark.parametrize("test_input,expected", test_delete_patient_account_test_data)
    def test_delete_patient_account(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        patient_object = Patient(database.patients_accounts)
        delete_result = patient_object.delete_patient_account(test_input[0])
        assert delete_result == expected

    # m.khazaee: this test must implement
    def test_edit_patient_account(self):
        assert False

    def test_show_patient_account(self):
        assert False

    def test_exist_patient(self):
        assert False

    def test_create_new_patient_account(self):
        assert False

    def test_index_of_patient(self):
        assert False

    #######################################
