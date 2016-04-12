Feature: User Login
  As the System Owner
  I want users to be able to login
  so that system can identify individual users
  and personalise services accordingly

  Scenario Outline: Existing user login
    Given at the login screen
    When an existing user submits the correct <InputUsername> and <inputPassword>
    Then the system should return "welcome username" as the authentication status of the user
    Examples:
      | InputUsername | inputPassword  |
      | mohamed     | 123456   |
      | admin    | qwerty     |


  Scenario Outline: Existing user (wrong password)
    Given at the login screen
    When an existing user submits the correct <InputUsername> but incorrect <inputPassword>
    Then the system should return "Wrong username or password" as the authentication status of the user
    Examples:
      | InputUsername | inputPassword  |
      | mohamed     | test12    |
      | admin     | 123456     |

  Scenario Outline: Unknown user
    Given at the login screen
    When an unknown user submits some <InputUsername> and <inputPassword>
    Then the system should return "Wrong username or password" as the authentication status of the user
    Examples:
      | InputUsername | inputPassword  |
      | batman   | batman    |
      | joo      | joo       |
