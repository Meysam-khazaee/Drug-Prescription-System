import pytest
import os
from pytest import MonkeyPatch
from source.drug import Drug
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


class TestDrug(object):
    exist_drug_test_data = [
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

    @pytest.mark.parametrize("test_input,expected", exist_drug_test_data)
    def test_exist_drug(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        drug_object = Drug(database.drugs_list)
        exist_result = drug_object.exist_drug(test_input[0])
        assert exist_result == expected

    delete_drug_test_data = [
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

    @pytest.mark.parametrize("test_input,expected", delete_drug_test_data)
    def test_delete_drug(self, setup, teardown, test_input, expected, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: test_input.pop(0))
        database = setup
        drug_object = Drug(database.drugs_list)
        delete_result = drug_object.delete_drug(test_input[0])
        assert delete_result == expected

    # m.khazaee: this test must implement
    def test_index_of_drug(self):
        assert False

    def test_add_drug(self):
        assert False

    def test_edit_drug(self):
        assert False

    def test_search_drug(self):
        assert False

    def test_show_drug_info(self):
        assert False

    ###############################