"""
Tests for Users Page
"""
from tests import test_package
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UsersTests(test_package.unittest.TestCase):
    log = test_package.cl.customLogger(test_package.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.us = test_package.Users(self.driver)
        self.ts = test_package.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_Users_200819_1(self):
        """
        Test for Dashboard link
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Users_200819_1 started")
        self.log.info("*#" * 20)
        self.us.gotoUsers()
        self.us.clickDashboard()
        result = self.us.verifyDashboard()
        self.ts.markFinal("test_TC_Users_200819_1", result, "Dashboard Link Verification")

    @pytest.mark.run(order=2)
    def test_TC_Users_200819_2(self):
        """
        Test for Create New User
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Users_200819_2 started")
        self.log.info("*#" * 20)
        self.us.gotoUsers()
        self.us.createUser(firstName="Test", lastName="Test", email="test@test.com", role="3")
        self.us.createUser(firstName="Test", lastName="Test 2", email="test2@test.com", role="3")
        result = self.us.verifyUser(email="test@test.com")
        self.ts.markFinal("test_TC_Users_200819_2", result, "Create New User Verification")

    @pytest.mark.run(order=3)
    def test_TC_Users_200819_3(self):
        """
        Test to verify view profile button
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Users_200819_3 started")
        self.log.info("*#" * 20)
        self.us.gotoUsers()
        self.us.clickViewProfile()
        result = self.us.verifyViewProfile()
        self.ts.markFinal("test_TC_Users_200819_3", result, "View profile button Verification")

    @pytest.mark.run(order=4)
    def test_TC_Users_UserProfile_200819_2(self):
        """
        Test for Teams working table open/close
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Users_UserProfile_200819_2 started")
        self.log.info("*#" * 20)
        self.us.gotoUsers()
        self.us.clickViewProfile()
        self.us.clickTeam()
        result = self.us.verifyTeamOpenClose()
        self.ts.mark(result=result, resultMessage="Teams Table Open Verification")
        self.us.clickTeam()
        result = self.us.verifyTeamOpenClose()
        result = not result
        self.ts.markFinal("test_TC_Users_UserProfile_200819_2", result, "Teams working table open/close Verification")

    @pytest.mark.run(order=5)
    def test_TC_Users_UserProfile_200819_4(self):
        """
        Test for team user details page
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Users_UserProfile_200819_4 started")
        self.log.info("*#" * 20)
        self.us.gotoUsers()
        self.us.clickViewProfile()
        self.us.clickTeam()
        self.us.clickDetails()
        result = self.us.verifyViewProfile()
        self.ts.markFinal("test_TC_Users_UserProfile_200819_4", result, "Teams working table open/close Verification")
