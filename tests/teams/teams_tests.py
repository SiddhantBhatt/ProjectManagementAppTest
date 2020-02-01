"""
Tests for Teams Page
"""
from tests import test_package
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TeamsTests(test_package.unittest.TestCase):
    log = test_package.cl.customLogger(test_package.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.tm = test_package.Teams(self.driver)
        self.ts = test_package.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_Teams_210819_1(self):
        """
        Test for Dashboard link
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_210819_1 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        self.tm.clickDashboard()
        result = self.tm.verifyDashboard()
        self.ts.markFinal("test_TC_Teams_210819_1", result, "Dashboard Link Verification")

    @pytest.mark.run(order=2)
    def test_TC_Teams_210819_2(self):
        """
        Test for Invalid Add Team
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_210819_2 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        result = self.tm.verifyInvalidTeam()
        self.ts.markFinal("test_TC_Teams_210819_2", result, "Add Invalid Team Verification")

    @pytest.mark.run(order=3)
    def test_TC_Teams_210819_3(self):
        """
        Test for Add Team
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_210819_3 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        self.tm.createTeam(name="Sample")
        self.tm.gotoTeams()
        result = self.tm.verifyTeam(name="Sample")
        self.ts.markFinal("test_TC_Teams_210819_3", result, "Add Team Verification")

    @pytest.mark.run(order=4)
    def test_TC_Teams_210819_4(self):
        """
        Test for Add Team Users
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_210819_4 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        self.tm.addTeamUsers(team="Sample", member1="Test Test", member2="Test Test 2")
        self.tm.gotoTeams()
        result = self.tm.verifyAddTeamUsers(teamName="Sample")
        self.ts.markFinal("test_TC_Teams_210819_4", result, "Add Team Users Verification")

    @pytest.mark.run(order=5)
    def test_TC_Teams_210819_5(self):
        """
        Test for View Members Table
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_210819_5 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        self.tm.clickViewMembers(teamName="Sample")
        result = self.tm.verifyMemberTable()
        self.ts.markFinal("test_TC_Teams_210819_5", result, "View Members Table Verification")

    @pytest.mark.run(order=6)
    def test_TC_Teams_TeamDetails_210819_1(self):
        """
        Test for View Members->View Profile Button
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Teams_TeamDetails_210819_1 started")
        self.log.info("*#" * 20)
        self.tm.gotoTeams()
        self.tm.clickViewMembers(teamName="Sample")
        self.tm.clickViewProfile(userName="Test Test")
        result = self.tm.verifyViewProfile(userName="Test Test")
        self.ts.markFinal("test_TC_Teams_TeamDetails_210819_1", result, "View Profile Button Verification")


