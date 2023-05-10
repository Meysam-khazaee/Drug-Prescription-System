# author = "meysam khazaee"
Feature: Check patient's account existence
  As a doctor, i want to check the patient's account existence
  so i should input the national code of patient
  then i get the result of the presence or absence of the patient's account
  Scenario Outline: Check patient's account existence
    Given As doctor i want to check patient's account existence
    When I entered the <national_code> as national code
    Then the result of existence will be <return_value>
    Examples:
    | national_code | return_value |
    | 4960011100    | True         |
    | 3860601325    | True         |
    | 4969053625    | True         |
    | 3860605783    | True         |
    | 4969604963    | True         |
    | 3872052053    | True         |
    | 3860960903    | True         |
    | 2366235390    | True         |
    | 23            | True         |
    | 4449665203    | False        |
    | 36            | False        |
    | 1110001110    | False        |
    | 3860062234    | False        |

