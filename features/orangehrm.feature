Feature: OrangeHRM Logo

 Scenario: Logo presence on OrangeHRM home page
  Given launch chrome browser
  When open orange hrm homepage
  Then verify that the logo present on page
  And close browser

# Scenario: Login to OrangeHRM site
#    Given launch chrome browser
#    When open orange hrm homepage
#    And Enter username and password
#    And click on Login button
#    Then User must be successfully login to home page