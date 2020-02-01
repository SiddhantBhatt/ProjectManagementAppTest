"""
All the Login page related methods will be present in this class
"""
from pages import page_package as pp
# import utilities.custom_logger as cl
# from pages.home.navigation_page import NavigationPage
# import logging
# from base.basepage import BasePage


class LoginPage(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _emailField = "materialContactFormName"
    _passwordField = "materialContactFormEmail"
    _loginButton = "//button[contains(text(),'Login Account')]"
    _errorText = "//h6[@class='text-danger']"
    _userDropdown = "navbarDropdownMenuLink-4"
    _logoutLink = "//a[contains(text(),'Logout')]"
    _forgotPassLink = "//a[contains(text(),'Forget Pasword ?')]"
    _resetButton = "//button[contains(text(),'CLick to Reset ')]"

    def logout(self):
        """
        Method to Logout the user
        """
        self.waitForElement(locator=self._userDropdown)
        self.elementClick(locator=self._userDropdown)
        self.elementClick(locator=self._logoutLink, locatorType="xpath")

    def login(self, email="", password=""):
        """
        Method to Login the user. Enters the email and password provided to the method
        """
        self.waitForElement(locator=self._emailField)
        self.clearField(locator=self._emailField)
        self.sendKeys(data=email, locator=self._emailField)
        self.clearField(locator=self._passwordField)
        self.sendKeys(data=password, locator=self._passwordField)
        self.elementClick(locator=self._loginButton, locatorType="xpath")

    def verifyInvalidLogin(self):
        """
        Verifies error message for invalid/failed login
        """
        self.waitForElement(locator=self._errorText, locatorType="xpath")
        result = self.isElementPresent(locator=self._errorText, locatorType="xpath")
        self.log.info("Invalid Login result: " + str(result))
        return result

    def verifySuccessfulLogin(self):
        """
        Checks for element from dashboard after logging in to verify
        """
        self.waitForElement(locator=self._userDropdown)
        result = self.isElementPresent(locator=self._userDropdown)
        self.log.info("Valid Login result: " + str(result))
        return result

    def forgotPassword(self, email=""):
        """
        Forgot password flow. Enters email provided to the method.
        """
        self.waitForElement(locator=self._forgotPassLink, locatorType="xpath")
        self.elementClick(locator=self._forgotPassLink, locatorType="xpath")
        self.waitForElement(locator=self._emailField)
        self.sendKeys(data=email, locator=self._emailField)
        self.elementClick(locator=self._resetButton, locatorType="xpath")

    def verifyInvalidForgotPassword(self):
        """
        Checks for error text displayed for invalid email entered for forgot password
        """
        self.waitForElement(locator=self._errorText, locatorType="xpath")
        result = self.isElementPresent(locator=self._errorText, locatorType="xpath")
        self.log.info("Invalid Forgot Password result: " + str(result))
        return result
