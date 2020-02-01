"""
All the Tickets page related methods will be present in this class
"""
from pages import page_package as pp


class Tickets(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _ticketsPageURL = "http://localhost/Arbeit/Board/TicketsDashboard"
    _dashboardBtn = "//a[contains(text(),'Dash')]"
    _verifyDashboardText = "//h5[contains(text(),'Recently Assigned Tickets')]"
    _filter_status = "statusListDTO"
    _ticketTable = "//table[@id='dtBasicExample']//tbody//tr"
    _table_statusColumn = "//table[@id='dtBasicExample']//tbody//tr[{}]//td[{}]"
    _ticketTitle = "//td[contains(text(),'{}')]"
    _ticketDetails_attachment = "//input[@id='File']"
    _ticketDetails_attachmentUploadCheckBtn = "//div[@id='button-row-attachement']//button[@title='Click here to send ']"
    _ticketDetails_attachmentSection = "attachment"
    _ticketDetails_attachment_file = "//div[@id='attachmentCollapse']//a[contains(text(),'{}')]"
    _searchBar = "//label[contains(text(),'Search:')]//input"
    _searchBtn = "search"
    _ticketTitleHeading = "//h2[contains(text(),'{}')]"
    _ticketDetails_editBtn = "//a[contains(text(),'Edit')]"
    _ticketDetails_edit_title = "ticketDTO_Title"
    _ticketDetails_edit_duration = "ticketDTO_Duration"
    _ticketDetails_edit_desc = "ticketDTO_Reason"
    _ticketDetails_edit_note = "ticketDTO_Note"
    _ticketDetails_edit_type = "ticketDTO_TypeId"
    _ticketDetails_edit_assign = "ticketDTO_AssignedUserId"
    _ticketDetails_edit_updateBtn = "//button[contains(text(),'Update Ticket')]"
    _ticketDetails_verifyEditTicket_type = "//span[contains(text(),'{}')]"
    _ticketDetails_verifyEditTicket_desc = "//div[contains(text(),'{}')]"
    _ticketDetails_verifyEditTicket_duration = "//span[contains(text(),'{} hrs')]"
    _ticketDetails_verifyEditTicket_note = "//div[contains(text(),'{}')]"
    _ticketDetails_verifyEditTicket_assign = "//div[contains(text(),'{}')]"
    _ticketDetails_ticketStatusDropdown = "StatusList"
    _ticketDetails_ticketStatusLabel = "status"
    _ticketDetails_commentTextbox = "commentDTO_Text"
    _ticketDetails_commentCheckBtn = "//div[@id='button-row-comment']//button[@title='Click here to send ']"
    _ticketDetails_commentSection = "comment"
    _ticketDetails_commentRecord = "//div[@id='commentCollapse']//div[contains(text(),'{}')]"
    _ticketDetails_commentModal = "commentCollapse"
    _ticketDetails_attachmentModal = "attachmentCollapse"
    _ticketDetails_commentCounter = "//div[contains(text(),'Comments')]//span"
    _ticketDetails_commentNumber = "//div[@id='commentCollapse']//div[@class='scroll-small']/child::div"
    _ticketDetails_attachmentCounter = "//div[contains(text(),'Attachment')]//span"
    _ticketDetails_attachmentNumber = "//div[@id='attachmentCollapse']//div[@class='scroll-small']/child::div"
    _ticketDetails_noCommentText = "//div[contains(text(),'No comment available right now')]"
    _ticketDetails_noAttachmentText = "//div[contains(text(),'No Attachement available right now')]"

    def gotoTickets(self):
        """
        Open tickets page URL
        """
        self.getURL(self._ticketsPageURL)

    def clickDashboard(self):
        """
        Method to Click on Dashboard Button and go to Dashboard Page
        """
        self.waitForElement(locator=self._dashboardBtn, locatorType="xpath")
        self.elementClick(locator=self._dashboardBtn, locatorType="xpath")

    def verifyDashboard(self):
        """
        Method to Verify navigation to Dashboard Page
        """
        self.waitForElement(locator=self._verifyDashboardText, locatorType="xpath")
        result = self.isElementPresent(locator=self._verifyDashboardText, locatorType="xpath")
        self.log.info("Click Dashboard Link result: " + str(result))
        return result

    def getTicketTable(self):
        """
        Get list of Ticket table rows WebElement object <tr>...</tr>
        """
        self.waitForElement(locator=self._ticketTable, locatorType="xpath")
        table = self.getElementList(locator=self._ticketTable, locatorType="xpath")
        return table

    def getColumnData(self, column):
        """
        Get data of the column provided in the argument from the table. Formats xpath according to column using dictionary
        """
        column = column.lower()
        column = column.strip()
        columnKeys = {'serial': 1, 'title': 2, 'type': 3, 'date': 4, 'duration': 5, 'assignto': 6, 'assignedby': 7, 'status': 8}
        columnNumber = columnKeys[column]
        table = self.getTicketTable()
        rows = len(table)
        columnRecords = []
        for i in range(1, rows+1):
            data = self.getText(locator=self._table_statusColumn.format(i, columnNumber), locatorType="xpath")
            columnRecords.append(data)
        return columnRecords

    def applyStatusFilter(self, status):
        """
        Apply status filter using the dropdown
        """
        self.waitForElement(locator=self._filter_status)
        self.selectBy(by="text", data=status, locator=self._filter_status)

    def verifyStatusFilter(self, status):
        """
        Verify if the selected filter was applied
        """
        statusList = self.getColumnData(column="status")
        result = True
        for data in statusList:
            if status in data:
                continue
            else:
                result = False
        self.log.info("Verify Status filter result: " + str(result))
        return result

    def clickTicket(self, title):
        """
        Click on a ticket
        """
        self.waitForElement(locator=self._ticketTitle.format(title), locatorType="xpath")
        self.elementClick(locator=self._ticketTitle.format(title), locatorType="xpath")

    def verifyClickTicket(self, title):
        """
        Verify Ticket was opened after clicking on it
        """
        self.waitForElement(locator=self._ticketTitleHeading.format(title), locatorType="xpath")
        result = self.isElementPresent(locator=self._ticketTitleHeading.format(title), locatorType="xpath")
        self.log.info("Verify Click Ticket result: " + str(result))
        return result

    def uploadAttachment(self, file):
        """
        Upload attachment in ticket. Browses asset directory folder to select and upload file
        """
        # Calculate File Path
        fileName = file
        assetDirectory = "../../assets/"
        relativeFileName = assetDirectory + fileName
        currentDirectory = pp.os.path.dirname(__file__)
        destinationFile = pp.os.path.abspath(pp.os.path.join(currentDirectory, relativeFileName))

        # self.waitForElement(locator=self._attachment, locatorType="xpath")
        self.sendKeys(data=destinationFile, locator=self._ticketDetails_attachment, locatorType="xpath")
        element = self.getElement(locator=self._ticketDetails_attachmentUploadCheckBtn, locatorType="xpath")
        self.driver.execute_script("arguments[0].click();", element)  # Click on hidden element

    def verifyUploadAttachment(self, file):
        """
        Verify for attachment upload
        """
        self.driver.refresh()
        self.attachmentExpandCollapse()
        result = self.isElementPresent(locator=self._ticketDetails_attachment_file.format(file), locatorType="xpath")
        self.log.info("Verify Upload attachment result: " + str(result))
        return result

    def openAttachment(self, file):
        """
        Click and open an attachment and verify(via URL) if the correct file was opened. Switches handle between tabs.
        """
        mainWindow = self.driver.current_window_handle
        self.waitForElement(locator=self._ticketDetails_attachmentSection)
        self.elementClick(locator=self._ticketDetails_attachmentSection)
        self.elementClick(locator=self._ticketDetails_attachment_file.format(file), locatorType="xpath")
        pp.time.sleep(1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(mainWindow)
        if file in url:
            self.log.info("Open attachment result: " + str(True))
            return True
        else:
            self.log.info("Open attachment result: " + str(False))
            return False

    def searchTicket(self, name):
        """
        Search for a ticket
        """
        self.waitForElement(locator=self._searchBar, locatorType="xpath")
        self.sendKeys(data=name, locator=self._searchBar, locatorType="xpath")
        self.elementClick(locator=self._searchBtn)

    def editTicket(self, title, duration, desc, note, ticketType, assign):
        """
        Edit an existing ticket using the arguments provided
        """
        self.waitForElement(locator=self._ticketDetails_editBtn, locatorType="xpath")
        self.elementClick(locator=self._ticketDetails_editBtn, locatorType="xpath")
        self.waitForElement(locator=self._ticketDetails_edit_title)
        self.clearField(locator=self._ticketDetails_edit_title)
        self.sendKeys(data=title, locator=self._ticketDetails_edit_title)
        self.clearField(locator=self._ticketDetails_edit_duration)
        self.sendKeys(data=duration, locator=self._ticketDetails_edit_duration)
        self.clearField(locator=self._ticketDetails_edit_desc)
        self.sendKeys(data=desc, locator=self._ticketDetails_edit_desc)
        self.clearField(locator=self._ticketDetails_edit_note)
        self.sendKeys(data=note, locator=self._ticketDetails_edit_note)
        self.selectBy(by="text", data=ticketType, locator=self._ticketDetails_edit_type)
        self.selectBy(by="text", data=assign, locator=self._ticketDetails_edit_assign)
        self.elementClick(locator=self._ticketDetails_edit_updateBtn, locatorType="xpath")

    def verifyEditTicket(self, title, duration, desc, note, ticketType, assign):
        """
        Verify Edit ticket. Checks each element and appends status in a list.
        """
        self.driver.refresh()
        resultList = []
        result = self.isElementPresent(locator=self._ticketTitleHeading.format(title), locatorType="xpath")
        resultList.append(result)
        result = self.isElementPresent(locator=self._ticketDetails_verifyEditTicket_duration.format(duration), locatorType="xpath")
        resultList.append(result)
        result = self.isElementPresent(locator=self._ticketDetails_verifyEditTicket_desc.format(desc), locatorType="xpath")
        resultList.append(result)
        result = self.isElementPresent(locator=self._ticketDetails_verifyEditTicket_note.format(note), locatorType="xpath")
        resultList.append(result)
        result = self.isElementPresent(locator=self._ticketDetails_verifyEditTicket_type.format(ticketType), locatorType="xpath")
        resultList.append(result)
        result = self.isElementPresent(locator=self._ticketDetails_verifyEditTicket_assign.format(assign), locatorType="xpath")
        resultList.append(result)
        if "False" in resultList:
            self.log.info("Verify Edit ticket result: " + str(False))
            return False
        else:
            self.log.info("Verify Edit Ticket result: " + str(True))
            return True

    def changeTicketStatus(self, status):
        """
        Method to change ticket status from the dropdown
        """
        self.waitForElement(locator=self._ticketDetails_ticketStatusDropdown)
        self.scrollIntoView(locator=self._ticketDetails_ticketStatusDropdown)
        self.selectBy(by="text", data=status, locator=self._ticketDetails_ticketStatusDropdown)

    def verifyTicketStatus(self, status):
        """
        Verify Ticket Status
        """
        text = self.getText(locator=self._ticketDetails_ticketStatusLabel)
        if text == status:
            self.log.info("Verify Ticket Status result: " + str(True))
            return True
        else:
            self.log.info("Verify Ticket Status result: " + str(False))
            return False

    def addComment(self, comment):
        """
        Add comment in a ticket
        """
        self.waitForElement(locator=self._ticketDetails_commentTextbox)
        self.elementClick(locator=self._ticketDetails_commentTextbox)
        self.sendKeys(data=comment, locator=self._ticketDetails_commentTextbox)
        self.elementClick(locator=self._ticketDetails_commentCheckBtn, locatorType="xpath")

    def verifyComment(self, comment):
        """
        Verify Comment display
        """
        self.driver.refresh()
        self.waitForElement(locator=self._ticketDetails_commentSection)
        self.elementClick(locator=self._ticketDetails_commentSection)
        result = self.isElementPresent(locator=self._ticketDetails_commentRecord.format(comment), locatorType="xpath")
        self.log.info("Verify Comment result: " + str(result))
        return result

    def commentExpandCollapse(self):
        """
        Expand/Collapse comment section
        """
        self.waitForElement(locator=self._ticketDetails_commentSection)
        self.elementClick(locator=self._ticketDetails_commentSection)

    def verifyCommentOpenClose(self):
        """
        Verify Comment section status (Expand/Collapse)
        """
        pp.time.sleep(1)
        element = self.getElement(locator=self._ticketDetails_commentModal)
        value = self.getAttribute(attribute="class", element=element)
        if "show" in value:
            self.log.info("Verify Comment Open/Close result: " + str(True))
            return True
        else:
            self.log.info("Verify Comment Open/Close result: " + str(False))
            return False

    def attachmentExpandCollapse(self):
        """
        Verify Attachment section status (Expand/Collapse)
        """
        self.waitForElement(locator=self._ticketDetails_attachmentSection)
        self.elementClick(locator=self._ticketDetails_attachmentSection)

    def verifyAttachmentOpenClose(self):
        pp.time.sleep(1)
        element = self.getElement(locator=self._ticketDetails_attachmentModal)
        value = self.getAttribute(attribute="class", element=element)
        if "show" in value:
            self.log.info("Verify Attachment Open/Close result: " + str(True))
            return True
        else:
            self.log.info("Verify Attachment Open/Close result: " + str(False))
            return False

    def verifyCommentCounter(self):
        """
        Verify whether comment counter is equal to the number of comments
        """
        self.waitForElement(locator=self._ticketDetails_commentCounter, locatorType="xpath")
        counter = self.getText(locator=self._ticketDetails_commentCounter, locatorType="xpath")
        self.commentExpandCollapse()
        if counter == "0":
            if self.isElementPresent(locator=self._ticketDetails_noCommentText, locatorType="xpath"):
                self.log.info("Verify Comment Counter result: " + str(True))
                return True
        else:
            commentList = self.getElementList(locator=self._ticketDetails_commentNumber, locatorType="xpath")
            totalComments = str(len(commentList))
            if counter == totalComments:
                self.log.info("Verify Comment Counter result: " + str(True))
                return True
        self.log.info("Verify Comment Counter result: " + str(False))
        return False

    def verifyAttachmentCounter(self):
        """
        Verify whether Attachment counter is equal to the number of comments
        """
        self.waitForElement(locator=self._ticketDetails_attachmentCounter, locatorType="xpath")
        self.scrollIntoView(locator=self._ticketDetails_attachmentCounter, locatorType="xpath")
        counter = self.getText(locator=self._ticketDetails_attachmentCounter, locatorType="xpath")
        self.attachmentExpandCollapse()
        if counter == "0":
            if self.isElementPresent(locator=self._ticketDetails_noAttachmentText, locatorType="xpath"):
                self.log.info("Verify Attachment Counter result: " + str(True))
                return True
        else:
            attachmentList = self.getElementList(locator=self._ticketDetails_attachmentNumber, locatorType="xpath")
            totalAttachments = str(len(attachmentList))
            if counter == totalAttachments:
                self.log.info("Verify Attachment Counter result: " + str(True))
                return True
        self.log.info("Verify Attachment Counter result: " + str(False))
        return False
