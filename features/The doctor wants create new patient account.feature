# author = "meysam khazaee"
Feature: create new patient account
  As a doctor I want to create new patient account
  so I enter patient information, If an account with new patient national code has not been created before
  then patient account created success.

  Scenario Outline: input patient information
    Given As doctor i want create patient account
    When I entered <name>, <lastname>, <national_code>, <birth_date>, <father_name>
    Then the result of new account creation will be <return_value>
    Examples:
    | name    | lastname   | national_code | birth_date |  father_name | return_value |
    | ali     | rezai      | 4960011011    | 2/4/1348   |  ahmad       | True         |
    | poria   | hamidi     | 3702125692    | 23/11/1341 |  farshad     | True         |
    | golsa   | shokri     | 1865923187    | 7/7/1332   |  abbdolla    | True         |
    | shayan  | bahiraie   | 14            | 18/2/1354  |  ali         | True         |
    | ali     | emamverdi  | 29            | 31/3/1376  |  mahmood     | True         |
    | zahra   | shamsi     | 86            | 10/7/1360  |  mahmood     | True         |