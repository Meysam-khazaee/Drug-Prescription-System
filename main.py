from source.database import Database
from source.login import Login
import os


def main():
    current_directory = os.getcwd()
    database_object = Database(current_directory)
    database_object.load_database()
    login_object = Login(database_object)
    login_object.display_menu()


if __name__ == '__main__':
    main()
