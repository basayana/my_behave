Feature: Enter Name and Email
Scenario Outline: enter name and email
    When enter <name> and <email>
    Examples:
    | name  | email              |
    | John  | john@example.com   |