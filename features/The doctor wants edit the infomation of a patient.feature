# author = "meysam khazaee"
Feature: Edit patient's account information
  As a doctor, i want to edit the patient's account information
  so i should input the national code of patient
  and if patient exist
  then i can edit information of patient.
  Scenario Outline: Edit patient's account information
    Given As doctor i want to edit the patient's account information
    When I input <national_code>, <name>, <lastname>, <birthdate>, <father_name> of patinet
    Then the result of edition will be <return_value>
    Examples:
      | national_code | name     | lastname  | birth_date | father_name | return_value |
      | 4960011100    | mohammad | rezai     | 2/4/1348   | ahmad       | True         |
      | 4960011012    | ali      | mohammadi | 8/5/1357   | reza        | False        |