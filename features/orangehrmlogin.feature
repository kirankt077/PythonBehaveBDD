Feature: OrangeHRM Login to site

  Scenario: Login to OrangeHRM site
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username "Admin" and password "admin123"
    And click on Login button
    Then User must be successfully login to home page


  Scenario Outline: Login to OrangeHRM site
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username "<username>" and password "<password>"
    And click on Login button
    Then User must be successfully login to home page
    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin    | admin123 |
      | admin123 | admin123 |

