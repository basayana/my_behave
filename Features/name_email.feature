Feature: Feature - Enter Name and Email
Scenario Outline: scenario - enter name and email
    When enter <name> and <email>
    Examples:
    | name  | email              |
    | John  | john@example.com   |