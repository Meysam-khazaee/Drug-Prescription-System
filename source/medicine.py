import time
from msvcrt import getch
import os


class Medicine:

    def __init__(self, medicines_list):
        self.medicines_list = medicines_list

    def exist_medicine(self, medicine_name):
        exist = False
        for med in self.medicines_list:
            if med[0] == medicine_name:
                exist = True
        return exist

    def index_of_medicine(self, medicine_name):
        if self.exist_medicine(medicine_name):
            for med in self.medicines_list:
                if med[0] == medicine_name:
                    return self.medicines_list.index(med)
        else:
            return -1

    def add_medicine(self, name, dos, max_dos, min_dos):
        med = [name, dos, max_dos, min_dos]
        if not (self.exist_medicine(med[0])):
            print("\n\tMedicine Information Created Successfully.")
            time.sleep(2)
            self.medicines_list.append(med)
            return True
        else:
            print("\n\tCreate Medicine Failed.(Medicine Existed)")
            time.sleep(2)
            return False

    def edit_medicine(self, medicine_name, newname, dos, max_dos, min_dos):
        index = self.index_of_medicine(medicine_name)
        if index != -1:
            self.medicines_list[index][0] = newname
            self.medicines_list[index][1] = dos
            self.medicines_list[index][2] = max_dos
            self.medicines_list[index][3] = min_dos
            os.system("cls")
            print("\n")
            self.show_medicine_info(index)
            print("\n\tMedicine Information Edited Successfully.")
            getch()
            return True
        else:
            print("\n\tEdit Medicine Failed.(Medicine Existed)")
            time.sleep(2)
            return False

    def search_medicine(self, medicine_name):
        index = self.index_of_medicine(medicine_name)
        if index != -1:
            print("\n")
            self.show_medicine_info(index)
            getch()
            return True
        else:
            print("\n\tMedicine with this name Not Exist.")
            time.sleep(2)
            return False

    def show_medicine_info(self, index_of_patient):
        print("\tMedicine {}:".format(index_of_patient + 1))
        print("\t\tName = {}".format(self.medicines_list[index_of_patient][0]))
        print("\t\tDos = {}".format(self.medicines_list[index_of_patient][1]))
        print("\t\tMax Dos = {}".format(self.medicines_list[index_of_patient][2]))
        print("\t\tMin Dos = {}".format(self.medicines_list[index_of_patient][3]))

    def delete_medicine(self, medicine_name):
        index = self.index_of_medicine(medicine_name)
        if index != -1:
            self.medicines_list.pop(index)
            print("\n\tMedicine Deleted Successfully.")
            time.sleep(1)
            return True
        else:
            print("\n\tMedicine with this name Not Exist.")
            time.sleep(1)
            return False
