# PythonBehaveBDD
PythonBehaveBDD with Seleinum

A BDD (Behavior-Driven Development) framework is a set of tools and a development process that uses plain, human-readable language to define software behavior and user requirements. It fosters collaboration between technical and non-technical stakeholders, creating "executable specifications" in a shared language like Gherkin, which are then used for automated testing to ensure the software meets business needs. Popular BDD frameworks include Cucumber and SpecFlow, often used with programming languages like Java, Python, and JavaScript.

What it is:
A development methodology: BDD focuses on how a user will interact with the software and the observable behaviors of the system. 
A collaborative tool: It brings together business stakeholders, product owners, testers, and developers to create a shared understanding of the requirements. 
Executable specifications: Requirements are written as user stories or scenarios in a simple, structured format using keywords like Given, When, and Then. 

How it works:
Define behavior: Stakeholders collaborate to write scenarios in a plain English format that describes the desired user experience. 
Use plain language: Tools like Cucumber use Gherkin, a natural language syntax, to write these "feature files" that define the behavior. 
Automate tests: The Gherkin scenarios are then linked to automated tests, allowing the team to verify that the software behaves as expected. 
Serve as documentation: The feature files also act as living documentation, providing clear, readable descriptions of the software's functionality for everyone on the team. 

What is behave?
> Behave is behaviour driven development
> Behave operates on directories containing:
> feature files written by Business Analyst/Sponsor/whoever with your behaviour scenarios in it and
> a steps directory with python step implementation for the scenarios.

BDD Scenarios and Features Files in Gherkin
Given,When,Then this are Gherkin keywords

Scenario: [Title/short discription]
> Given [A precondition]
> When [Some evenr]
> Then [Some outcome]

Example - 
Feature: OrangeHRM Login

Scenario: Logo presence on OrangeHRM home page
    * Given I launch chrome browser
    * When I open orange hrm homepage
    * Then verify that the logo present on page

Scenario: Login to OrangeHRM site
    Given I launch chrome browser
    When I open orange hrm homepage
    And Enter username and password
    And click on Login button
    Then User must be successfully login to home page

    
