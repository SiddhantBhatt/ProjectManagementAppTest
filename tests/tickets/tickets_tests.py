"""
Tests for Tickets Page
"""
from tests import test_package as tp
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TicketsTests(tp.unittest.TestCase):
    log = tp.cl.customLogger(tp.logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.tk = tp.Tickets(self.driver)
        self.ts = tp.TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_TC_TicketsDashboard_220819_1(self):
        """
        Test for Dashboard link
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_220819_1 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickDashboard()
        result = self.tk.verifyDashboard()
        self.ts.markFinal("test_TC_TicketsDashboard_220819_1", result, "Dashboard Link Verification")

    @pytest.mark.run(order=2)
    def test_TC_TicketsDashboard_220819_2(self):
        """
        Test for Status Filter
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_220819_2 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.applyStatusFilter(status="Active")
        result = self.tk.verifyStatusFilter(status="Active")
        self.ts.markFinal("test_TC_TicketsDashboard_220819_2", result, "Status Filter Verification")

    @pytest.mark.run(order=3)
    def test_TC_TicketsDashboard_220819_4(self):
        """
        Test for Click Ticket
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_220819_4 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        result = self.tk.verifyClickTicket(title="Sample Ticket")
        self.ts.markFinal("test_TC_TicketsDashboard_220819_4", result, "Click Ticket Verification")

    @pytest.mark.run(order=4)
    def test_TC_TicketsDashboard_TicketDetails_220819_1(self):
        """
        Test for Dashboard link
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_1 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.clickDashboard()
        result = self.tk.verifyDashboard()
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_1", result, "Dashboard Link Verification")

    @pytest.mark.run(order=5)
    def test_TC_TicketsDashboard_TicketDetails_220819_2(self):
        """
        Test for Edit Ticket
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_2 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.editTicket(title="Sample Ticket Edit", duration="5", desc="Sample Ticket Edit", note="Sample Ticket Edit", ticketType="Bug / Issues", assign="Test Test 2")
        result = self.tk.verifyEditTicket(title="Sample Ticket Edit", duration="5", desc="Sample Ticket Edit", note="Sample Ticket Edit", ticketType="Bug / Issues", assign="Test Test 2")
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_2", result, "Edit Ticket Verification")

    @pytest.mark.run(order=6)
    def test_TC_TicketsDashboard_TicketDetails_220819_3(self):
        """
        Test for Change ticket status
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_3 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.changeTicketStatus(status="In Progress")
        result = self.tk.verifyTicketStatus(status="In Progress")
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_3", result, "Change ticket status Verification")

    @pytest.mark.run(order=7)
    def test_TC_TicketsDashboard_TicketDetails_220819_4(self):
        """
        Test for Add Comment
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_4 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.addComment(comment="Test")
        result = self.tk.verifyComment(comment="Test")
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_4", result, "Add Comment Verification")

    @pytest.mark.run(order=8)
    def test_TC_TicketsDashboard_TicketDetails_220819_6(self):
        """
        Test for Expand/Collapse Comments section
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_6 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.commentExpandCollapse()
        result = self.tk.verifyCommentOpenClose()
        self.ts.mark(result=result, resultMessage="Expand Comment section Verification")
        self.tk.commentExpandCollapse()
        result = self.tk.verifyCommentOpenClose()
        result = not result
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_6", result, "Expand/Collapse Comments section Verification")

    @pytest.mark.run(order=9)
    def test_TC_TicketsDashboard_TicketDetails_220819_7(self):
        """
        Test for Upload attachment
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_7 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.uploadAttachment(file="Note.txt")
        result = self.tk.verifyUploadAttachment(file="Note.txt")
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_7", result, "Upload attachment Verification")

    @pytest.mark.run(order=10)
    def test_TC_TicketsDashboard_TicketDetails_220819_9(self):
        """
        Test for Expand/Collapse Comments section
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_9 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        self.tk.attachmentExpandCollapse()
        result = self.tk.verifyAttachmentOpenClose()
        self.ts.mark(result=result, resultMessage="Expand Attachment section Verification")
        self.tk.attachmentExpandCollapse()
        result = self.tk.verifyAttachmentOpenClose()
        result = not result
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_9", result, "Expand/Collapse Attachment section Verification")

    @pytest.mark.run(order=11)
    def test_TC_TicketsDashboard_TicketDetails_220819_10(self):
        """
        Test for opening attachment
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_10 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        result = self.tk.openAttachment(file="Note.txt")
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_10", result, "Open attachment Verification")

    @pytest.mark.run(order=11)
    def test_TC_TicketsDashboard_TicketDetails_220819_11(self):
        """
        Test for comparing comment counter and total comments
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_TC_TicketsDashboard_TicketDetails_220819_11 started")
        self.log.info("*#" * 20)
        self.tk.gotoTickets()
        self.tk.clickTicket(title="Sample Ticket")
        result = self.tk.verifyCommentCounter()
        self.ts.mark(result=result, resultMessage="Comment Counter-Number Verification")
        result = self.tk.verifyAttachmentCounter()
        self.ts.markFinal("test_TC_TicketsDashboard_TicketDetails_220819_11", result, "Attachment-Comment Counter Verification")
