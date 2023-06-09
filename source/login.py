import os
import time

from source.doctor import Doctor
from source.drug import Drug
from source.patient import Patient
from source.visit import Visit
from msvcrt import getch


class Login:

    def __init__(self, database):
        self.database = database
        self.log_validation = False
        self.logged_doctor = None

    def log_in(self, username, password):
        for dc in self.database.doctors_accounts:
            if dc[3] == username and dc[4] == password:
                self.log_validation = True
                self.logged_doctor = Doctor(dc[0], dc[1], dc[2], dc[3], dc[4])
        return self.log_validation

    def display_menu(self):

        while True:
            os.system('cls')
            print('\n---------------- Drug Prescription System ----------------\n')
            print("\t1.Login\n\t2.Exit/Quit")
            choose = input("\n\tWhat would you like to do? ")
            if choose == "1":
                os.system('cls')
                print('\n---------------- Login Panel ----------------\n')
                user = input("\tUsername = ")
                password = input("\tPassword = ")

                if self.log_in(user, password):
                    print("\n\tYou logged in successfully.")
                    time.sleep(2)

                    while True:

                        os.system('cls')
                        print('\n---------------- Welcome Drug Prescription System ----------------\n')
                        print("Hi Doctor < %s, %s > :" % (
                            self.logged_doctor.d_name, self.logged_doctor.d_lastname))
                        print("\n\t1.Patient Management\n\t2.Drug Management\n\t3.Patient Visit\n\t4.Logout")
                        ans = input("\n\tWhat would you like to do? ")
                        if ans == "1":

                            os.system('cls')
                            print('\n---------------- Patient Panel ----------------\n')
                            print("\t1.Create New Patient Account\n\t2.Edit Patient Account\n\t3.Search Patient "
                                  "Account\n\t4.Delete Patient Account\n\t5.Back")
                            ch = input("\n\tWhat would you like to do? ")

                            p = Patient(self.database.patients_accounts)

                            if ch == "1":
                                os.system('cls')
                                print('\n---------------- Create Patient Account ----------------\n')
                                name = input("\tPatient name = ")
                                lastname = input("\tPatient lastname = ")
                                national_code = input("\tPatient national_code = ")
                                birth_date = input("\tPatient birth_date = ")
                                father_name = input("\tPatient father_name = ")
                                p.create_new_patient_account(name, lastname, national_code, birth_date, father_name)
                                self.database.save_database()

                            elif ch == "2":
                                os.system('cls')
                                print('\n---------------- Edit Patient Account ----------------\n')
                                national_code = input("Enter National Code = ")
                                name = input("\n\tNew patient name = ")
                                lastname = input("\tNew patient lastname = ")
                                birth_date = input("\tNew patient birth_date = ")
                                father_name = input("\tNew patient father_name = ")
                                p.edit_patient_account(national_code, name, lastname, birth_date, father_name)
                                self.database.save_database()

                            elif ch == "3":
                                os.system('cls')
                                print('\n---------------- Search(Show) Patient Account ----------------\n')
                                p.search_patient_account(input("\n\tEnter National Code = "))
                                self.database.save_database()

                            elif ch == "4":
                                os.system('cls')
                                print('\n---------------- Delete Patient Account ----------------\n')
                                p.delete_patient_account(input("\n\tEnter National Code = "))
                                self.database.save_database()

                            elif ch == "5":
                                continue

                            else:
                                print('\n\tInvalid Choice Try Again.')
                                time.sleep(2)

                        elif ans == "2":
                            os.system('cls')
                            print('\n---------------- Drug Panel ----------------\n')
                            print(
                                "\t1.Add Drug info\n\t2.Edit Drug info\n\t3.Search Drug "
                                "info\n\t4.Delete Drug info\n\t5.Back")
                            ch = input("\n\tWhat would you like to do? ")

                            drug = Drug(self.database.drugs_list)

                            if ch == "1":
                                os.system('cls')
                                print('\n---------------- Add Drug ----------------\n')
                                name = input("\n\tDrug name = ")
                                dos = float(input("\tDrug dos = "))
                                max_dos = float(input("\tDrug Max-Dos = "))
                                min_dos = float(input("\tDrug Min-Dos = "))
                                drug.add_drug(name, dos, max_dos, min_dos)
                                self.database.save_database()

                            elif ch == "2":
                                os.system('cls')
                                print('\n---------------- Edit Drug ----------------\n')
                                name = input("\n\tEnter Drug Name = ")
                                newname = input("\tDrug New name = ")
                                dos = float(input("\tDrug New dos = "))
                                max_dos = float(input("\tDrug New Max-Dos = "))
                                min_dos = float(input("\tDrug New Min-Dos = "))
                                drug.edit_drug(name, newname, dos, max_dos, min_dos)
                                self.database.save_database()

                            elif ch == "3":
                                os.system("cls")
                                print("\n---------- Searched Drug Information ----------")
                                drug.search_drug(input("\n\tEnter Drug Name = "))
                                self.database.save_database()

                            elif ch == "4":
                                drug.delete_drug(input("\n\tEnter Drug Name = "))
                                self.database.save_database()

                            elif ch == "5":
                                continue

                            else:
                                print('\n\tInvalid Choice Try Again.\n')
                                time.sleep(2)

                        elif ans == "3":
                            os.system('cls')
                            patient_drug_list = []
                            print('\n-------------------------- Visit Panel --------------------------\n')
                            patient_national_code = input("\tEnter National Code = ")
                            p = Patient(self.database.patients_accounts)
                            while True:
                                os.system('cls')
                                print('-------------------------- Visit Panel --------------------------\n')
                                print('\tPatient < {0}, {1} >\n'.format(
                                    self.database.patients_accounts[p.index_of_patient(patient_national_code)][0],
                                    self.database.patients_accounts[p.index_of_patient(patient_national_code)][1]))

                                print(
                                    "\t1.Select Drug From Previous Prescriptions\n\t2.Select Drug From "
                                    "Drugs List\n\t3.Show And Confirm Current Prescriptions\n\t4.Back")
                                ch = input("\n\tWhat would you like to do? ")
                                visit_obj = Visit(self.database.patients_accounts, self.database.drugs_list, patient_drug_list)
                                if ch == "1":
                                    patient_drug_list.append(visit_obj.previous_prescriptions(patient_national_code))
                                elif ch == "2":
                                    input_char = input("\n\tEnter First Character The Drug You Want = ")
                                    patient_drug_list.append(visit_obj.prescribe_from_drugs_list(input_char))
                                elif ch == "3":
                                    os.system("cls")
                                    print("\n\t--------- Current Prescriptions ---------\n")
                                    for med in patient_drug_list:
                                        if med is not None:
                                            print("\t{}".format(med), end="")
                                    char = input("\n\tDo you want to finalize the prescription??(y,n) ")
                                    if char == 'y':
                                        print("\n\tPrescriptions Printed Successfully.")
                                        time.sleep(2)
                                        visit_obj.report(patient_national_code)
                                        return 0
                                elif ch == "4":
                                    break
                                else:
                                    print('\n\tInvalid Choice Try Again.\n')
                                    time.sleep(2)

                        elif ans == "4":
                            os.system("cls")
                            print("\n\t<<  Hope to see you again.Goodbye  >>")
                            return 0
                        else:
                            print("\n\tNot Valid. Press a key and Try again")
                            time.sleep(2)
                else:
                    print('\n\tInvalid Username Or Password.\n\tPlease Choose Again.')
                    time.sleep(2)

            elif choose == "2":
                os.system("cls")
                print("\n\t<<  Hope to see you again.Goodbye  >>")
                time.sleep(2)
                self.database.save_database()
                return True
            else:
                print('\n\tInvalid Choice.\n\tPlease Press a Key and Choose Again.')
                time.sleep(2)
