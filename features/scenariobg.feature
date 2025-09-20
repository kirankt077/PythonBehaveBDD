Feature: OrangeHRM Login to site

  Background: common steps
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username "Admin" and password "admin123"
    And click on Login button

  Scenario: Login to OrangeHRM site
    Then User must be successfully login to home page


  Scenario: Able to Search user
    When navigate to search page
    Then search page should display

  Scenario: Able to perform Advance Search user all
    When navigate to advance search page
    Then advance search page should display

