import time
import os
from msvcrt import getch


class Patient:

    def __init__(self, patients_accounts):
        self.patients_accounts = patients_accounts

    def exist_patient(self, national_code):
        exist = False
        for patient in self.patients_accounts:
            if patient[2] == national_code:
                exist = True
        return exist

    def create_new_patient_account(self, name, lastname, national_code, birth_date, father_name):
        patient_account = [name, lastname, national_code, birth_date, father_name]
        if not (self.exist_patient(patient_account[2])):
            print("\n\tPatient Account Created Successfully.")
            time.sleep(2)
            self.patients_accounts.append(patient_account)
            return True
        else:
            print("\n\tCreate Patient Account Failed.(Patient Existed)")
            time.sleep(2)
            return False

    def index_of_patient(self, national_code):
        if self.exist_patient(national_code):
            for patient in self.patients_accounts:
                if patient[2] == national_code:
                    return self.patients_accounts.index(patient)
        else:
            return -1

    def search_patient_account(self, national_code):
        index = self.index_of_patient(national_code)
        if index != -1:
            os.system("cls")
            print("\n---------- Searched Patient Account ----------")
            self.show_patient_account(index)
            time.sleep(2)
            return True
        else:
            print("\n\tPatient with this National Code Not Exist.")
            time.sleep(2)
            return False

    def edit_patient_account(self, national_code, name, lastname, birthdate, father_name):
        index = self.index_of_patient(national_code)
        if index != -1:
            self.patients_accounts[index][0] = name
            self.patients_accounts[index][1] = lastname
            self.patients_accounts[index][3] = birthdate
            self.patients_accounts[index][4] = father_name
            os.system("cls")
            print("\n")
            self.show_patient_account(index)
            print("\n\tPatient Account Edited Successfully.")
            time.sleep(2)
            return True
        else:
            print("\n\tPatient with this National Code Not Exist.")
            time.sleep(2)
            return False

    def show_patient_account(self, index_of_patient):
        print("\tPatient {}:".format(index_of_patient + 1))
        print("\t\tName = {}".format(self.patients_accounts[index_of_patient][0]))
        print("\t\tLast Name = {}".format(self.patients_accounts[index_of_patient][1]))
        print("\t\tNational Code = {}".format(self.patients_accounts[index_of_patient][2]))
        print("\t\tBirth Data = {}".format(self.patients_accounts[index_of_patient][3]))
        print("\t\tFather Name = {}".format(self.patients_accounts[index_of_patient][4]))

    def delete_patient_account(self, national_code):
        index = self.index_of_patient(national_code)
        if index != -1:
            self.patients_accounts.pop(index)
            print("\n\tPatient Account Deleted Successfully.")
            time.sleep(2)
            return True
        else:
            print("\n\tPatient with this National Code Not Exist.")
            time.sleep(2)
            return False
