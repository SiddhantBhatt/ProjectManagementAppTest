"""
All the Dashboard page related methods will be present in this class
"""
from pages import page_package as pp


class Dashboard(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _navBar_boards = "//a[contains(text(),'Boards')]"
    _navBar_teams = "//a[contains(text(),'Teams')]"
    _navBar_users = "//a[contains(text(),'Users')]"
    _navBar_reports = "//a[contains(text(),'| Reports')]"
    _navBar_myAccount = "//a[contains(text(),'My Account')]"
    _logoutLink = "//a[contains(text(),'Logout')]"
    _userDropdown = "navbarDropdownMenuLink-4"
    _boards_verifyText = "//h4[contains(text(),'All Availble Boards')]"
    _teams_verifyText = "//h4[contains(text(),'All Availble Teams')]"
    _users_verifyText = "//h4[contains(text(),'All Availble Users')]"
    _myAccount_verify = "profile-pic"
    _loginButton = "//button[contains(text(),'Login Account')]"
    _home = "//a[contains(text(),'Arbeit')]"
    _assignedTickets_from = "fromAs"
    _assignedTickets_to = "toAs"
    _assignedTickets_go = "filterAs"
    _unassignedTickets_from = "fromUn"
    _unassignedTickets_to = "toUn"
    _unassignedTickets_go = "filterUn"

    def gotoHome(self):
        """
        Click on 'Arbeit' link and go to home page
        """
        self.elementClick(locator=self._home, locatorType="xpath")

    def clickLink(self, locator, locatorType):
        """
        Common method to wait for an element and clicking on it. Works on element with provided argument values
        """
        self.waitForElement(locator=locator, locatorType=locatorType)
        self.elementClick(locator=locator, locatorType=locatorType)

    def verifyclickLink(self, locator, locatorType):
        """
        Common method to verify the loaded page after clicking on a link
        """
        self.waitForElement(locator=locator, locatorType=locatorType)
        result = self.isElementPresent(locator=locator, locatorType=locatorType)
        return result

    def boardsLink(self):
        """
        Click on Boards link and verify Boards page opening
        """
        self.clickLink(locator=self._navBar_boards, locatorType="xpath")
        result = self.verifyclickLink(locator=self._boards_verifyText, locatorType="xpath")
        self.log.info("Click Boards Link result: " + str(result))
        return result

    def teamsLink(self):
        """
        Click on Teams link and verify Teams page opening
        """
        self.clickLink(locator=self._navBar_teams, locatorType="xpath")
        result = self.verifyclickLink(locator=self._teams_verifyText, locatorType="xpath")
        self.log.info("Click Teams Link result: " + str(result))
        return result

    def usersLink(self):
        """
        Click on Users link and verify Users page opening
        """
        self.clickLink(locator=self._navBar_users, locatorType="xpath")
        result = self.verifyclickLink(locator=self._users_verifyText, locatorType="xpath")
        self.log.info("Click Users Link result: " + str(result))
        return result

    def myAccountLink(self):
        """
        Click on My Account link and verify My account object display
        """
        self.clickLink(locator=self._userDropdown, locatorType="id")
        self.clickLink(locator=self._navBar_myAccount, locatorType="xpath")
        result = self.verifyclickLink(locator=self._myAccount_verify, locatorType="id")
        self.log.info("Click My Account Link result: " + str(result))
        return result

    def logoutLink(self):
        """
        Click on Logout link and verify logged out page
        """
        self.clickLink(locator=self._userDropdown, locatorType="id")
        self.clickLink(locator=self._logoutLink, locatorType="xpath")
        result = self.verifyclickLink(locator=self._loginButton, locatorType="xpath")
        self.log.info("Click Logout Link result: " + str(result))
        return result

    def assignedTicketsFilter(self, fromDate, toDate, help="mm/dd/yyyy"):
        """
        Enter dates(arguments) into ticket filter input box
        """
        try:
            self.sendKeys(fromDate, locator=self._assignedTickets_from)
            self.sendKeys(toDate, locator=self._assignedTickets_to)
            self.elementClick(locator=self._assignedTickets_go)
            return True
        except:
            return False

    def unassignedTicketsFilter(self, fromDate, toDate, help="mm/dd/yyyy"):
        """
        Enter dates(arguments) into ticket filter input box
        """
        try:
            self.sendKeys(fromDate, locator=self._unassignedTickets_from)
            self.sendKeys(toDate, locator=self._unassignedTickets_to)
            self.elementClick(locator=self._unassignedTickets_go)
            return True
        except:
            return False
