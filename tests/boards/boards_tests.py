"""
Tests for Boards Page
"""
from tests import test_package
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BoardsTests(test_package.unittest.TestCase):
    log = test_package.cl.customLogger(test_package.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.bd = test_package.Boards(self.driver)
        self.ts = test_package.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_Boards_210819_1(self):
        """
        Test for Dashboard link
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_210819_1 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickDashboard()
        result = self.bd.verifyDashboard()
        self.ts.markFinal("test_TC_Boards_210819_1", result, "Dashboard Link Verification")

    @pytest.mark.run(order=2)
    def test_TC_Boards_210819_2(self):
        """
        Test for Create Board case
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_210819_2 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.createBoard(name="Sample", desc="Sample", team="Sample")
        self.bd.gotoBoards()
        result = self.bd.verifyCreateBoard(name="Sample")
        self.ts.markFinal("test_TC_Boards_210819_2", result, "Create Board Verification")

    @pytest.mark.run(order=3)
    def test_TC_Boards_210819_3(self):
        """
        Test for Open Board Details Page
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_210819_3 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        result = self.bd.verifyClickBoard(name="Sample")
        self.ts.markFinal("test_TC_Boards_210819_3", result, "Open Board Details Page Verification")

    @pytest.mark.run(order=4)
    def test_TC_Boards_BoardDetails_220819_1(self):
        """
        Test for Clicking back to dashboard button
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_220819_1 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickBackToDashboard()
        result = self.bd.verifyDashboard()
        self.ts.markFinal("test_TC_Boards_BoardDetails_220819_1", result, "Clicking back to dashboard button Verification")

    @pytest.mark.run(order=5)
    def test_TC_Boards_BoardDetails_220819_3(self):
        """
        Test for creating a list
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_220819_3 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.addNewList(listName="Sample List")
        self.bd.addNewList(listName="Sample List 2")
        result = self.bd.verifyAddList(listName="Sample List")
        self.ts.markFinal("test_TC_Boards_BoardDetails_220819_3", result, "Create a list Verification")

    @pytest.mark.run(order=6)
    def test_TC_Boards_BoardDetails_220819_4(self):
        """
        Test for creating a card
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_220819_4 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.addNewCard(listName="Sample List", cardTitle="Sample Card", cardDesc="Sample Card")
        self.bd.addNewCard(listName="Sample List", cardTitle="Sample Card 2", cardDesc="Sample Card 2")
        result = self.bd.verifyAddNewCard(listName="Sample List", cardTitle="Sample Card")
        self.ts.markFinal("test_TC_Boards_BoardDetails_220819_4", result, "Create a card Verification")

    @pytest.mark.run(order=7)
    def test_TC_Boards_BoardDetails_220819_5(self):
        """
        Test for Opening List->Card
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_220819_5 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card")
        result = self.bd.verifyAddNewCard(listName="Sample List", cardTitle="Sample Card")
        self.ts.markFinal("test_TC_Boards_BoardDetails_220819_5", result, "Opening List->Card Verification")

    @pytest.mark.run(order=8)
    def test_TC_Boards_BoardDetails_CardDetails_220819_1(self):
        """
        Test for Create Ticket
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_CardDetails_220819_1 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card")
        self.bd.addTicket(title="Sample Ticket", duration="4", desc="Sample Ticket", note="Sample Ticket", ticketType="Task", user="Test Test")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card")
        self.bd.clickAllTickets()
        result = self.bd.verifyaddTicket(title="Sample Ticket")
        self.ts.markFinal("test_TC_Boards_BoardDetails_CardDetails_220819_1", result, "Create Ticket Verification")

    @pytest.mark.run(order=9)
    def test_TC_Boards_BoardDetails_CardDetails_220819_2(self):
        """
        Test for Move Card
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_CardDetails_220819_2 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card 2")
        self.bd.moveCard(moveTo="Sample List 2")
        result = self.bd.verifyMoveCard(listName="Sample List 2", cardTitle="Sample Card 2")
        self.ts.markFinal("test_TC_Boards_BoardDetails_CardDetails_220819_2", result, "Move Card Verification")

    @pytest.mark.run(order=10)
    def test_TC_Boards_BoardDetails_CardDetails_220819_3(self):
        """
        Test for Edit Card
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_CardDetails_220819_3 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card 2")
        self.bd.editCard(desc="Sample Card 2 Edited")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card 2")
        result = self.bd.verifyEditCard(desc="Sample Card 2 Edited")
        self.ts.markFinal("test_TC_Boards_BoardDetails_CardDetails_220819_3", result, "Edit Card Verification")

    @pytest.mark.run(order=11)
    def test_TC_Boards_BoardDetails_CardDetails_220819_4(self):
        """
        Test for All tickets button
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_Boards_BoardDetails_CardDetails_220819_4 started")
        self.log.info("*#" * 20)
        self.bd.gotoBoards()
        self.bd.clickBoard(name="Sample")
        self.bd.clickCard(listName="Sample List", cardTitle="Sample Card")
        self.bd.clickAllTickets()
        result = self.bd.verifyclickAllTicket()
        self.ts.markFinal("test_TC_Boards_BoardDetails_CardDetails_220819_4", result, "All tickets button Verification")


