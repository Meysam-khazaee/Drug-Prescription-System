# author = "meysam khazaee"
Feature: Sign in to patient admission and drug administration system
    As a doctor, I want to sign in to system
    So I should get the welcome message after login.
    Scenario Outline: sign in to patient admission and drug administration system
        Given sign in doctor to system
        When As a doctor, I have to enter my <username> and <password>.
        Then The return value of my login process to system will be <validation>.
        Examples:
            | username  | password | validation |
            | meysam_kh | 1332     | True       |
            | milad_ma  | 1234     | True       |
            | hasan     | 4567     | False      |
            | hacker    | 6789     | False      |