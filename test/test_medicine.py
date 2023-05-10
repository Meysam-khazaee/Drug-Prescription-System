import pytest
import os
from pytest import MonkeyPatch
from source.medicine import Medicine
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


class TestMedicine(object):
    exist_medicine_test_data = [
        (["Acetaminophen"], True),
        (["Amitriptyline"], True),
        (["Farxiga"], True),
        (["Invokana"], True),
        (["Meloxicam"], True),
        (["Naltrexone"], True),
        (["Onpattro"], True),
        (["Pantoprazole"], True),
        (["Dupixent"], True),
        (["Wellbutrin"], True),
        (["weqwewqe"], False),
        (["wqewq"], False),
    ]

    @pytest.mark.parametrize("test_input,expected", exist_medicine_test_data)
    def test_exist_medicine(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        medicine_object = Medicine(database.medicines_list)
        exist_result = medicine_object.exist_medicine(test_input[0])
        assert exist_result == expected

    def test_index_of_medicine(self):
        assert False

    def test_add_medicine(self):
        assert False

    def test_edit_medicine(self):
        assert False

    def test_search_medicine(self):
        assert False

    def test_show_medicine_info(self):
        assert False

    delete_medicine_test_data = [
        (["Acetaminophen"], True),
        (["Amitriptyline"], True),
        (["Farxiga"], True),
        (["Invokana"], True),
        (["Meloxicam"], True),
        (["Naltrexone"], True),
        (["Onpattro"], True),
        (["Pantoprazole"], True),
        (["Dupixent"], True),
        (["Wellbutrin"], True),
        (["weqwewqe"], False),
        (["wqewq"], False),
    ]

    @pytest.mark.parametrize("test_input,expected", delete_medicine_test_data)
    def test_delete_medicine(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        medicine_object = Medicine(database.medicines_list)
        delete_result = medicine_object.delete_medicine(test_input[0])
        assert delete_result == expected
