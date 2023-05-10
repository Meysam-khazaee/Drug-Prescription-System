#######################################################
# 
# Login.py
# Python implementation of the Class Login
# Generated by Enterprise Architect
# Created on:      06-May-2023 12:08:55 AM
# Original author: Meysam
# 
#######################################################
from source.Visit import Visit
from source.Medicine import Medicine
from source.Patient import Patient
from source.Doctor import Doctor

class Login(Visit, Medicine, Patient, Doctor):
    def __init__(self, database):
        pass

    def log_in(self, username, password):
        pass

    def display_menu(self):
        pass