import os


class Database:

    def __init__(self, root_directory):
        self.database_directory = "{0}\\database".format(root_directory)
        self.patients_accounts = []
        self.doctors_accounts = []
        self.drugs_list = []

    def load_database(self):
        file_path = "{0}\\patients_accounts.txt".format(self.database_directory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as opened_file:
                self.patients_accounts = opened_file.read().splitlines()
                for i in range(len(self.patients_accounts)):
                    self.patients_accounts[i] = self.patients_accounts[i].split(',')

        file_path = "{0}\\doctors_accounts.txt".format(self.database_directory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as opened_file:
                self.doctors_accounts = opened_file.read().splitlines()
                for i in range(len(self.doctors_accounts)):
                    self.doctors_accounts[i] = self.doctors_accounts[i].split(',')

        file_path = "{0}\\drugs_list.txt".format(self.database_directory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as opened_file:
                self.drugs_list = opened_file.read().splitlines()
                for i in range(len(self.drugs_list)):
                    self.drugs_list[i] = self.drugs_list[i].split(',')

    def save_database(self):

        file_path = "{0}\\patients_accounts.txt".format(self.database_directory)
        with open(file_path, 'w') as opened_file:
            for patient in self.patients_accounts:
                opened_file.write("{},{},{},{},{}\n".format(patient[0], patient[1], patient[2], patient[3], patient[4]))

        file_path = "{0}\\doctors_accounts.txt".format(self.database_directory)
        with open(file_path, 'w') as opened_file:
            for doctor in self.doctors_accounts:
                opened_file.write("{},{},{},{},{}\n".format(doctor[0], doctor[1], doctor[2], doctor[3], doctor[4]))

        file_path = "{0}\\drugs_list.txt".format(self.database_directory)
        with open(file_path, 'w') as opened_file:
            for drug in self.drugs_list:
                opened_file.write("{},{},{},{}\n".format(drug[0], drug[1], drug[2], drug[3]))

