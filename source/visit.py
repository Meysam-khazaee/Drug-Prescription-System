import os
import time
import glob
from pathlib import Path
from source.patient import Patient
from msvcrt import getch


class Visit:

    def __init__(self, patients_accounts, medicines_list, patient_medicine_list):
        self.patients_accounts = patients_accounts
        self.medicines_list = medicines_list
        self.patient_medicine_list = patient_medicine_list

    def report(self, patient_national_code):
        valid = False
        patient_database_directory = "{0}\\Database\\prescriptions_database".format(os.getcwd())
        os.chdir(patient_database_directory)
        opened_file = open(r"{}.txt".format(patient_national_code), 'a')
        for medic_list in self.patient_medicine_list:
            if medic_list is not None:
                opened_file.write(medic_list)
                valid = True
        return valid

    def previous_prescriptions(self, patient_national_code):
        p = Patient(self.patients_accounts)
        if p.exist_patient(patient_national_code):
            root_directory = os.getcwd()
            database_directory = "{0}\\database\\prescriptions_database".format(root_directory)
            os.chdir(database_directory)
            exist = False
            file_list = []
            for file_name in glob.glob("*.txt"):
                if file_name == ("{}.txt".format(patient_national_code)):
                    file_list = Path(file_name).read_text().splitlines()
                    exist = True
            if exist:
                while True:
                    os.system('cls')
                    temp_file_list = []
                    print('---------------- Previous Medicine <Patient: {} {}> ----------------\n'.format(
                        self.patients_accounts[p.index_of_patient(patient_national_code)][0],
                        self.patients_accounts[p.index_of_patient(patient_national_code)][1]))
                    i = 0
                    for i in range(len(file_list)):
                        print("\t{}.{}".format(i + 1, file_list[i]))
                        temp_file_list.append(file_list[i].split(','))
                    ch = int(input("\n\tWhat Medicine would you Want to choose? "))
                    if ch in range(1, len(temp_file_list) + 1):
                        print("\n\t------------------------------------")
                        print("\tSelected Medicine = {}".format(temp_file_list[ch - 1][0]))
                        dos = float(input("\tSet Dos = "))
                        if (dos >= (float(temp_file_list[ch - 1][2]))) and (
                                dos <= float(temp_file_list[ch - 1][3])):
                            char = input("\tThe inputted dose is within the allowable range.\n\n\tDo you confirm?(y,n)")
                            if char == 'y':
                                print("\t------------------------------------")
                                print("\tMedicine Added To Prescriptions Successfully.\n\tPress any key to go back.")
                                getch()
                                os.chdir(root_directory)
                                return (
                                    "{},{},{},{}\n".format(temp_file_list[int(ch) - 1][0], dos,
                                                           temp_file_list[int(ch) - 1][2],
                                                           temp_file_list[int(ch) - 1][3]))
                            else:
                                print("\t------------------------------------")
                                print("\tMedicine Add To Prescriptions Failed\n\tYou will be returned to the "
                                      "previous step by press any key.")
                                getch()
                                break
                        else:
                            print("\n\tThe set dose not in range.\n\tPress a key and return to previous menu.")
                            getch()
                            break
                    else:
                        print('\n\tInvalid Choice.\n\tPlease Press a Key and Choose Again.')
                        getch()
            else:
                print("\n\tPatient Not Have Previous Prescriptions.")
                time.sleep(2)
            os.chdir(root_directory)
        else:
            print("\n\tPatient with this National Code Not Exist.\n\tYou will be returned to the previous step.")
            time.sleep(2)

    def prescribe_from_medicines_list(self, input_char):
        while True:
            list_med = []
            j = 1
            i = 0
            for i in range(len(self.medicines_list)):
                if self.medicines_list[i][0][0].lower() == input_char.lower():
                    j += 1
                    list_med.append(self.medicines_list[i])

            if j > 1:
                os.system("cls")
                print("\n--------------- Searched Medicine With First Character <{},{}> ---------------\n".format(
                    input_char.lower(), input_char.upper()))
                for i in range(j - 1):
                    print("\t{}.{}".format(i + 1, list_med[i][0]))
                ch = int(input("\n\tWhat Medicine would you Want to choose? "))
                if ch in range(1, len(list_med) + 1):
                    print("\n\t------------------------------------")
                    print("\tSelected Medicine = {}".format(list_med[int(ch) - 1][0]))
                    dos = float(input("\tSet Dos = "))
                    if (dos >= (float(list_med[ch - 1][2]))) and (
                            dos <= float(list_med[ch - 1][3])):
                        char = input("\tThe inputted dose is within the allowable range.\n\n\tDo you confirm?(y,n)")
                        if char == 'y':
                            print("\t------------------------------------")
                            print("\tMedicine Added To Prescriptions Successfully.\n\tPress any key to go back.")
                            getch()
                            return (
                                "{},{},{},{}\n".format(list_med[int(ch) - 1][0], dos,
                                                       list_med[int(ch) - 1][2], list_med[int(ch) - 1][3]))
                        else:
                            print("\t------------------------------------")
                            print("\tMedicine Add To Prescriptions Failed\n\tYou will be returned to the "
                                  "previous step by press any key.")
                            getch()
                            break
                    else:
                        print("\n\tThe set dose not in range.\n\tPress a key and return to previous menu.")
                        getch()
                        break

                else:
                    print('\tInvalid Choice.Press any key and Try Again.')
                    getch()


            else:
                print("\n\tThere are no drugs that start with this word in the database.\n\tPress a key to go back.")
                getch()
                break
