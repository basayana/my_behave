Feature: test shadowDOM
Scenario: shadowDOM
    Given open browser with URL https://testautomationpractice.blogspot.com/
    when get shadow DOM object
    then close browser