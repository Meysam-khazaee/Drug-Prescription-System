import os
import time
import glob
from pathlib import Path
from source.patient import Patient
from msvcrt import getch


class Visit:

    def __init__(self, patients_accounts, drugs_list, patient_drug_list):
        self.patients_accounts = patients_accounts
        self.drugs_list = drugs_list
        self.patient_drug_list = patient_drug_list

    def report(self, patient_national_code):
        valid = False
        patient_database_directory = "{0}\\Database\\prescriptions_database".format(os.getcwd())
        os.chdir(patient_database_directory)
        opened_file = open(r"{}.txt".format(patient_national_code), 'a')
        for drug_list in self.patient_drug_list:
            if drug_list is not None:
                opened_file.write(drug_list)
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
                    print('---------------- Previous Drug <Patient: {} {}> ----------------\n'.format(
                        self.patients_accounts[p.index_of_patient(patient_national_code)][0],
                        self.patients_accounts[p.index_of_patient(patient_national_code)][1]))
                    i = 0
                    for i in range(len(file_list)):
                        print("\t{}.{}".format(i + 1, file_list[i]))
                        temp_file_list.append(file_list[i].split(','))
                    ch = int(input("\n\tWhat Drug would you Want to choose? "))
                    if ch in range(1, len(temp_file_list) + 1):
                        print("\n\t------------------------------------")
                        print("\tSelected Drug = {}".format(temp_file_list[ch - 1][0]))
                        dos = float(input("\tSet Dos = "))
                        if (dos >= (float(temp_file_list[ch - 1][2]))) and (
                                dos <= float(temp_file_list[ch - 1][3])):
                            char = input("\tThe inputted dose is within the allowable range.\n\n\tDo you confirm?(y,n)")
                            if char == 'y':
                                print("\t------------------------------------")
                                print("\tDrug Added To Prescriptions Successfully.\n\tPress any key to go back.")
                                time.sleep(2)
                                os.chdir(root_directory)
                                return (
                                    "{},{},{},{}\n".format(temp_file_list[int(ch) - 1][0], dos,
                                                           temp_file_list[int(ch) - 1][2],
                                                           temp_file_list[int(ch) - 1][3]))
                            else:
                                print("\t------------------------------------")
                                print("\tDrug Add To Prescriptions Failed\n\tYou will be returned to the "
                                      "previous step by press any key.")
                                time.sleep(2)
                                break
                        else:
                            print("\n\tThe set dose not in range.\n\tPress a key and return to previous menu.")
                            time.sleep(2)
                            break
                    else:
                        print('\n\tInvalid Choice.\n\tPlease Press a Key and Choose Again.')
                        time.sleep(2)
            else:
                print("\n\tPatient Not Have Previous Prescriptions.")
                time.sleep(2)
            os.chdir(root_directory)
        else:
            print("\n\tPatient with this National Code Not Exist.\n\tYou will be returned to the previous step.")
            time.sleep(2)

    def prescribe_from_drugs_list(self, input_char):
        while True:
            list_drug = []
            j = 1
            i = 0
            for i in range(len(self.drugs_list)):
                if self.drugs_list[i][0][0].lower() == input_char.lower():
                    j += 1
                    list_drug.append(self.drugs_list[i])

            if j > 1:
                os.system("cls")
                print("\n--------------- Searched Drug With First Character <{},{}> ---------------\n".format(
                    input_char.lower(), input_char.upper()))
                for i in range(j - 1):
                    print("\t{}.{}".format(i + 1, list_drug[i][0]))
                ch = int(input("\n\tWhat Drug would you Want to choose? "))
                if ch in range(1, len(list_drug) + 1):
                    print("\n\t------------------------------------")
                    print("\tSelected Drug = {}".format(list_drug[int(ch) - 1][0]))
                    dos = float(input("\tSet Dos = "))
                    if (dos >= (float(list_drug[ch - 1][2]))) and (
                            dos <= float(list_drug[ch - 1][3])):
                        char = input("\tThe inputted dose is within the allowable range.\n\n\tDo you confirm?(y,n)")
                        if char == 'y':
                            print("\t------------------------------------")
                            print("\tDrug Added To Prescriptions Successfully.\n\tPress any key to go back.")
                            time.sleep(2)
                            return (
                                "{},{},{},{}\n".format(list_drug[int(ch) - 1][0], dos,
                                                       list_drug[int(ch) - 1][2], list_drug[int(ch) - 1][3]))
                        else:
                            print("\t------------------------------------")
                            print("\tDrug Add To Prescriptions Failed\n\tYou will be returned to the "
                                  "previous step by press any key.")
                            time.sleep(2)
                            break
                    else:
                        print("\n\tThe set dose not in range.\n\tPress a key and return to previous menu.")
                        time.sleep(2)
                        break

                else:
                    print('\tInvalid Choice.Press any key and Try Again.')
                    time.sleep(2)

            else:
                print("\n\tThere are no drugs that start with this word in the database.\n\tPress a key to go back.")
                time.sleep(2)
                break
