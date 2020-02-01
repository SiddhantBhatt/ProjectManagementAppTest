"""
Tests for Dashboard Page
"""
from tests import test_package
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DashboardTests(test_package.unittest.TestCase):
    log = test_package.cl.customLogger(test_package.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.db = test_package.Dashboard(self.driver)
        self.lp = test_package.LoginPage(self.driver)
        self.ts = test_package.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_Home_Dashboard_NavBar_190819_1to6(self):
        """
        Tests for Dashboard Navbar links
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Home_Dashboard_NavBar_190819_1to6 started")
        self.log.info("*#" * 20)
        result = self.db.boardsLink()
        self.ts.mark(result=result, resultMessage="Boards Link Verification")
        self.db.gotoHome()
        result = self.db.teamsLink()
        self.ts.mark(result=result, resultMessage="Teams Link Verification")
        self.db.gotoHome()
        result = self.db.usersLink()
        self.ts.mark(result=result, resultMessage="Users Link Verification")
        self.db.gotoHome()
        result = self.db.myAccountLink()
        self.ts.mark(result=result, resultMessage="My Account Link Verification")
        self.db.gotoHome()
        result = self.db.logoutLink()
        self.ts.markFinal("test_TC_Home_Dashboard_NavBar_190819_1to6", result, "Navbar links Verification")

    @pytest.mark.run(order=2)
    def test_TC_Home_Dashboard_190819_6(self):
        """
        Tests for Ticket Filters
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Home_Dashboard_190819_6 started")
        self.log.info("*#" * 20)
        self.lp.login("siddhantb@mindfiresolutions.com", "mindfire")
        result = self.db.assignedTicketsFilter(fromDate="08262019", toDate="08262019")
        self.ts.mark(result=result, resultMessage="Assigned Filter Verification")
        result = self.db.unassignedTicketsFilter(fromDate="08262019", toDate="08262019")
        self.ts.markFinal("test_TC_Home_Dashboard_190819_6", result, "Ticket Filter Verification")
        test_package.time.sleep(4)
