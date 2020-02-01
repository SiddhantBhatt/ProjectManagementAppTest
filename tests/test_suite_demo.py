"""
Demo test suite file
"""

import unittest
from tests.home.login_tests import LoginTests
from tests.home.dashboard_tests import DashboardTests
from tests.users.users_tests import UsersTests
from tests.teams.teams_tests import TeamsTests
from tests.boards.boards_tests import BoardsTests
from tests.tickets.tickets_tests import TicketsTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(DashboardTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(UsersTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TeamsTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(BoardsTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(TicketsTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
