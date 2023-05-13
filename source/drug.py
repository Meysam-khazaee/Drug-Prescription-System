import time
from msvcrt import getch
import os


class Drug:

    def __init__(self, drugs_list):
        self.drugs_list = drugs_list

    def exist_drug(self, drug_name):
        exist = False
        for drug in self.drugs_list:
            if drug[0] == drug_name:
                exist = True
        return exist

    def index_of_drug(self, drug_name):
        if self.exist_drug(drug_name):
            for drug in self.drugs_list:
                if drug[0] == drug_name:
                    return self.drugs_list.index(drug)
        else:
            return -1

    def add_drug(self, name, dos, max_dos, min_dos):
        drug = [name, dos, max_dos, min_dos]
        if not (self.exist_drug(drug[0])):
            print("\n\tDrug Information Created Successfully.")
            time.sleep(2)
            self.drugs_list.append(drug)
            return True
        else:
            print("\n\tCreate Drug Failed.(Drug Existed)")
            time.sleep(2)
            return False

    def edit_drug(self, drug_name, newname, dos, max_dos, min_dos):
        index = self.index_of_drug(drug_name)
        if index != -1:
            self.drugs_list[index][0] = newname
            self.drugs_list[index][1] = dos
            self.drugs_list[index][2] = max_dos
            self.drugs_list[index][3] = min_dos
            os.system("cls")
            print("\n")
            self.show_drug_info(index)
            print("\n\tDrug Information Edited Successfully.")
            time.sleep(2)
            return True
        else:
            print("\n\tEdit Drug Failed.(Drug Existed)")
            time.sleep(2)
            return False

    def search_drug(self, drug_name):
        index = self.index_of_drug(drug_name)
        if index != -1:
            print("\n")
            self.show_drug_info(index)
            time.sleep(2)
            return True
        else:
            print("\n\tDrug with this name Not Exist.")
            time.sleep(2)
            return False

    def show_drug_info(self, index_of_patient):
        print("\tDrug {}:".format(index_of_patient + 1))
        print("\t\tName = {}".format(self.drugs_list[index_of_patient][0]))
        print("\t\tDos = {}".format(self.drugs_list[index_of_patient][1]))
        print("\t\tMax Dos = {}".format(self.drugs_list[index_of_patient][2]))
        print("\t\tMin Dos = {}".format(self.drugs_list[index_of_patient][3]))

    def delete_drug(self, drug_name):
        index = self.index_of_drug(drug_name)
        if index != -1:
            self.drugs_list.pop(index)
            print("\n\tDrug Deleted Successfully.")
            time.sleep(1)
            return True
        else:
            print("\n\tDrug with this name Not Exist.")
            time.sleep(1)
            return False
