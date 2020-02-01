"""
Tests for Login Page
"""
from tests import test_package
import pytest

# from pages.home.login_page import LoginPage
# from utilities.teststatus import TestStatus
# import unittest
# import pytest
# import utilities.custom_logger as cl
# import logging
# import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(test_package.unittest.TestCase):
    log = test_package.cl.customLogger(test_package.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.lp = test_package.LoginPage(self.driver)
        self.ts = test_package.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_Home_Login_190819_1(self):
        """
        Tests for invalid login test case
        Logs out first because of oneTimeSetup Login
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Home_Login_190819_1 started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("siddhantb@mindfiresolutions.com", "mindfir")
        result = self.lp.verifyInvalidLogin()
        self.ts.markFinal("test_TC_Home_Login_190819_1", result, "Invalid Login Verification")

    @pytest.mark.run(order=2)
    def test_TC_Home_Login_190819_2(self):
        """
        Tests for valid login test case
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Home_Login_190819_2 started")
        self.log.info("*#" * 20)
        self.lp.login("siddhantb@mindfiresolutions.com", "mindfire")
        result = self.lp.verifySuccessfulLogin()
        self.ts.markFinal("test_TC_Home_Login_190819_2", result, "Valid Login Verification")

    @pytest.mark.run(order=3)
    def test_TC_Home_Login_ForgotPassword_190819_2(self):
        """
        Tests for invalid(email) forgot password case
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Home_Login_ForgotPassword_190819_2 started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.forgotPassword(email="sidb@xyz.com")
        result = self.lp.verifyInvalidForgotPassword()
        self.ts.markFinal("test_TC_Home_Login_ForgotPassword_190819_2", result, "invalid(email) forgot password Verification")