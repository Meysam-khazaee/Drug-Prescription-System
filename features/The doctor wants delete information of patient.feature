# author = "meysam khazaee"
Feature: Delete patient's account
  As a doctor, i want to delete the patient's account
  so i should input the national code of patient
  then i get the result of the delete process.
  Scenario Outline: Delete patient's account existence
    Given As doctor i want to delete patient's account
    When I input the <national_code> of patient as national code
    Then the result of delete process will be <return_value>
    Examples:
    | national_code | return_value |
    | 4960011100    | True         |
    | 3860601325    | True         |
    | 4969053625    | True         |
    | 23            | True         |
    | 4449665203    | False        |
    | 36            | False        |
    | 1110001110    | False        |
    | 3860062234    | False        |

