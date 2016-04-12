# Created by Mohamed_86 at 3/27/2016
Feature: As a system owner, I want users to be able to sign up,
         so that the system can save necessary to identify and verify individual user.

  Scenario Outline: user already exist 
    Given  at the Sign-Up page
    When   the <inputName> or <inputEmail> is already exist. it does not matter if <inputPassword> is exist or not.
    Then   the system should return "Your Account has been successfully registered" as the registration status of the user
	Examples:
      | inputName  | inputEmail             | inputPassword |
      | mohamed   | mohamed@gmail.com | 123456   |
      | admin     | ray@yahoo.com     | 123456   |
	  | ray       | admin@admin.com   | 123456   |
  Scenario Outline: new user
    Given  at the Sign-Up page
    When   the <inputName> or <inputEmail> is not exist in db. it does not matter if <inputPassword> is exist or not.
    Then   the system should return "user already exists in the current database" as the registration status of the user
	Examples:
      | inputName  | inputEmail             | inputPassword |
      | mike      | mike@gmail.com    | 123456   |
      | ray       | ray@yahoo.com     | 123456   |