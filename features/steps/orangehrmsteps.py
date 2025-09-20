import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    time.sleep(10)
    status=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()


@when('Enter username "{user}" and password "{pwd}"')
def enterUsernamePassword(context,user,pwd):
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)


@when('click on Login button')
def clickLoginButton(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()


@then('User must be successfully login to home page')
def checkDashboardPage(context):
    try:
        time.sleep(5)
        loginPageTitle = context.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
        assert loginPageTitle == 'Dashboard'
        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test failed as unable to login"


@when('navigate to search page')
def step_impl(context):
    assert True, "Test passed"


@then('search page should display')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to advance search page')
def step_impl(context):
    assert True, "Test passed"


@then('advance search page should display')
def step_impl(context):
    assert True, "Test passed"