"""
All the Boards page related methods will be present in this class
"""
from pages import page_package as pp


class Boards(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _navBar_boards = "//a[contains(text(),'Boards')]"
    _dashboardBtn = "//a[contains(text(),'Dash')]"
    _verifyDashboardText = "//h5[contains(text(),'Recently Assigned Tickets')]"
    _createBoardBtn = "//button[@data-target='#modalBoardForm']"
    _createBoard_name = "boardDTO_Title"
    _createBoard_desc = "boardDTO_Description"
    _createBoard_selectTeam = "boardDTO_CompanyTeamId"
    _createBoard_addBoardBtn = "//button[contains(text(),'Add Board')]"
    _boardText = "//h5[contains(text(),'{}')]"
    _boardPage_name = "//div[contains(text(),'{}')]"
    _boardDetails_backToDashBtn = "//a[contains(text(),'Back to DashBoard')]"
    _boardDetails_addNewListBtn = "//div[@id='accordionEx4']//h5[@class='mb-0']"
    _boardDetails_listTitleField = "ListTitle"
    _boardDetails_addListBtn = "//div[@id='AddListCollapse']//button[contains(text(),'Add now')]"
    _boardDetails_verifyList = "//div[@class='card-title row'][contains(text(),'{}')]"
    _boardDetails_addNewCard = "//div[@class='card-title row'][contains(text(),'{}')]/following-sibling::div//h5[@class='mb-0']"
    _boardDetails_addNewCard_cardTitle = "//div[@class='card-title row'][contains(text(),'{}')]/following-sibling::div//input[@id='cardDTO_Title']"
    _boardDetails_addNewCard_cardDesc = "//div[@class='card-title row'][contains(text(),'{}')]/following-sibling::div//input[@id='cardDTO_Description']"
    _boardDetails_addNewCard_addNowBtn = "//div[@class='card-title row'][contains(text(),'{}')]/following-sibling::div//button[contains(text(),'Add now')]"
    _boardDetails_cardText = "//div[@class='card-title row'][contains(text(),'{}')]/following-sibling::div//div[contains(text(),'{}')]"
    _boardDetails_cardModal = "modalRegisterForm"
    _cardDetails_addTicketBtn = "//button[contains(text(),'+ Ticket')]"
    _cardDetails_allTicketsBtn = "//a[contains(text(),'All Tickets')]"
    _addTicket_title = "ticketDTO_Title"
    _addTicket_duration = "ticketDTO_Duration"
    _addTicket_desc = "ticketDTO_Reason"
    _addTicket_note = "ticketDTO_Note"
    _addTicket_type = "ticketDTO_TypeId"
    _addTicket_assignUser = "ticketDTO_AssignedUserId"
    _addTicket_createTicketBtn = "//button[contains(text(),'Create Ticket')]"
    _addTicket_verify = "//td[contains(text(),'{}')]"
    _cardDetails_moveTicketBtn = "//button[contains(text(),'Move')]"
    _cardDetails_moveToList = "//div[@class='row drop']//div[contains(text(),'{}')]"
    _cardDetails_description = "//textarea[@id='cardDTO_Description']"
    _cardDetails_saveBtn = "//button[contains(text(),'Save')]"
    _ticketsDashboardText = "//h4[contains(text(),'Tickets Dashboard')]"

    def gotoBoards(self):
        """
        Click on Boards link from header to go to Boards page
        """
        self.elementClick(locator=self._navBar_boards, locatorType="xpath")

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

    def createBoard(self, name, desc, team):
        """
        Method to Create new Board having the details provided(arguments).
        """
        self.waitForElement(locator=self._createBoardBtn, locatorType="xpath")
        self.elementClick(locator=self._createBoardBtn, locatorType="xpath")
        self.waitForElement(locator=self._createBoard_name)
        self.sendKeys(data=name, locator=self._createBoard_name)
        self.sendKeys(data=desc, locator=self._createBoard_desc)
        self.selectBy(by="text", data=team, locator=self._createBoard_selectTeam)
        self.elementClick(locator=self._createBoard_addBoardBtn, locatorType="xpath")

    def verifyCreateBoard(self, name):
        """
        Verify Board Creation
        """
        self.waitForElement(locator=self._boardText.format(name), locatorType="xpath")
        result = self.isElementPresent(locator=self._boardText.format(name), locatorType="xpath")
        self.log.info("Create Board result: " + str(result))
        return result

    def clickBoard(self, name):
        """
        Click on Board having the provided name(argument)
        """
        self.waitForElement(locator=self._boardText.format(name), locatorType="xpath")
        self.elementClick(locator=self._boardText.format(name), locatorType="xpath")

    def verifyClickBoard(self, name):
        """
        Verify Board page display
        """
        self.waitForElement(locator=self._boardPage_name.format(name), locatorType="xpath")
        result = self.isElementPresent(locator=self._boardPage_name.format(name), locatorType="xpath")
        self.log.info("Click Board result: " + str(result))
        return result

    def clickBackToDashboard(self):
        """
        Method to Click on Dashboard Button and go to Dashboard Page
        """
        self.waitForElement(locator=self._boardDetails_backToDashBtn, locatorType="xpath")
        self.elementClick(locator=self._boardDetails_backToDashBtn, locatorType="xpath")

    def addNewList(self, listName):
        """
        Create new list with provided listname
        """
        self.scrollIntoView(locator=self._boardDetails_addNewListBtn, locatorType="xpath")
        self.waitForElement(locator=self._boardDetails_addNewListBtn, locatorType="xpath")
        self.elementClick(locator=self._boardDetails_addNewListBtn, locatorType="xpath")
        self.sendKeys(data=listName, locator=self._boardDetails_listTitleField)
        self.elementClick(locator=self._boardDetails_addListBtn, locatorType="xpath")
        self.driver.refresh()

    def verifyAddList(self, listName):
        """
        Verify New list creation
        """
        self.waitForElement(locator=self._boardDetails_verifyList.format(listName), locatorType="xpath")
        result = self.isElementPresent(locator=self._boardDetails_verifyList.format(listName), locatorType="xpath")
        self.log.info("Verify Add List result: " + str(result))
        return result

    def addNewCard(self, listName, cardTitle, cardDesc):
        """
        Add/Create a card inside a list. Uses provided arguments for card data.
        """
        self.waitForElement(locator=self._boardDetails_addNewCard.format(listName), locatorType="xpath")
        self.elementClick(locator=self._boardDetails_addNewCard.format(listName), locatorType="xpath")
        self.sendKeys(data=cardTitle, locator=self._boardDetails_addNewCard_cardTitle.format(listName), locatorType="xpath")
        self.sendKeys(data=cardDesc, locator=self._boardDetails_addNewCard_cardDesc.format(listName), locatorType="xpath")
        self.elementClick(locator=self._boardDetails_addNewCard_addNowBtn.format(listName), locatorType="xpath")

    def verifyAddNewCard(self, listName, cardTitle):
        self.waitForElement(locator=self._boardDetails_cardText.format(listName, cardTitle), locatorType="xpath")
        result = self.isElementPresent(locator=self._boardDetails_cardText.format(listName, cardTitle), locatorType="xpath")
        self.log.info("Verify Add new card result: " + str(result))
        return result

    def clickCard(self, listName, cardTitle):
        """
        Method to click on a card
        """
        self.waitForElement(locator=self._boardDetails_cardText.format(listName, cardTitle), locatorType="xpath")
        self.elementClick(locator=self._boardDetails_cardText.format(listName, cardTitle), locatorType="xpath")

    def verifyClickCard(self):
        """
        Verify Card details modal when clicking on a card
        """
        text = self.getAttribute(attribute="class", locator=self._boardDetails_cardModal)
        if "show" in text:
            self.log.info("Verify Click Card result: " + str(True))
            return True
        else:
            self.log.info("Verify Click Card result: " + str(False))
            return False

    def addTicket(self, title, duration, desc, note, ticketType, user):
        """
        Add/Create ticket inside a card. Uses ticket data provided in the arguments.
        """
        self.waitForElement(locator=self._cardDetails_addTicketBtn, locatorType="xpath")
        self.elementClick(locator=self._cardDetails_addTicketBtn, locatorType="xpath")
        self.waitForElement(locator=self._addTicket_title)
        self.sendKeys(data=title, locator=self._addTicket_title)
        self.sendKeys(data=duration, locator=self._addTicket_duration)
        self.sendKeys(data=desc, locator=self._addTicket_desc)
        self.sendKeys(data=note, locator=self._addTicket_note)
        self.selectBy(by="text", data=ticketType, locator=self._addTicket_type)
        self.selectBy(by="text", data=user, locator=self._addTicket_assignUser)
        self.elementClick(locator=self._addTicket_createTicketBtn, locatorType="xpath")

    def clickAllTickets(self):
        """
        Click on All Tickets button
        """
        self.waitForElement(locator=self._cardDetails_allTicketsBtn, locatorType="xpath")
        self.elementClick(locator=self._cardDetails_allTicketsBtn, locatorType="xpath")

    def verifyaddTicket(self, title):
        """
        Verify ticket creation
        """
        self.waitForElement(locator=self._addTicket_verify.format(title), locatorType="xpath")
        result = self.isElementPresent(locator=self._addTicket_verify.format(title), locatorType="xpath")
        self.log.info("Verify Add Ticket result: " + str(result))
        return result

    def moveCard(self, moveTo):
        """
        Move a card from one list to another.
        """
        self.waitForElement(locator=self._cardDetails_moveTicketBtn, locatorType="xpath")
        self.elementClick(locator=self._cardDetails_moveTicketBtn, locatorType="xpath")
        self.waitForElement(locator=self._cardDetails_moveToList.format(moveTo), locatorType="xpath")
        self.elementClick(locator=self._cardDetails_moveToList.format(moveTo), locatorType="xpath")
        alert = self.waitForAlert()
        alert.accept()

    def verifyMoveCard(self, listName, cardTitle):
        """
        Verify Move Card feature
        """
        result = self.verifyAddNewCard(listName=listName, cardTitle=cardTitle)
        self.log.info("Verify Move card result: " + str(result))
        return result

    def editCard(self, desc):
        """
        Edit an existing card details
        """
        self.waitForElement(locator=self._cardDetails_description, locatorType="xpath")
        self.clearField(locator=self._cardDetails_description, locatorType="xpath")
        self.sendKeys(data=desc, locator=self._cardDetails_description, locatorType="xpath")
        self.elementClick(locator=self._cardDetails_saveBtn, locatorType="xpath")

    def verifyEditCard(self, desc):
        """
        Verify Card Edit feature
        """
        text = self.getText(locator=self._cardDetails_description, locatorType="xpath")
        if text == desc:
            self.log.info("Verify Edit Card result: " + str(True))
            return True
        else:
            self.log.info("Verify Edit Card result: " + str(False))
            return False

    def verifyclickAllTicket(self):
        """
        Verifies All tickets page display
        """
        self.waitForElement(locator=self._ticketsDashboardText, locatorType="xpath")
        result = self.isElementPresent(locator=self._ticketsDashboardText, locatorType="xpath")
        self.log.info("Verify Click All Ticket result: " + str(result))
        return result


