"""
All the Users page related methods will be present in this class
"""
from pages import page_package as pp


class Users(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _navBar_users = "//a[contains(text(),'Users')]"
    _dashboardBtn = "//a[contains(text(),'Dash')]"
    _verifyDashboardText = "//h5[contains(text(),'Recently Assigned Tickets')]"
    _createUserBtn = "//button[contains(text(),'+ Create New User')]"
    _createUser_firstName = "companyUserDTO_FirstName"
    _createUser_lastName = "companyUserDTO_LastName"
    _createUser_email = "companyUserDTO_Email"
    _createUser_role = "companyUserDTO_RoleId"
    _createUser_addUserBtn = "//button[contains(text(),'Add User')]"
    _verifyUserEmail = "//td[contains(text(),'{}')]"
    _viewProfileBtn = "//a[contains(text(),'View Profile')]"
    _viewProfileImg = "//img[@alt='Profile Image']"
    _userProfile_team = "//div[@class='card-header']//table[@class='table text-primary']"
    _userProfile_membersTable = "collapseTwo1_20030"
    _userProfile_detailsBtn = "//a[contains(text(),'Details')]"

    def gotoUsers(self):
        """
        Method to Click on Users Link and go to Users Page
        """
        self.elementClick(locator=self._navBar_users, locatorType="xpath")

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

    def createUser(self, firstName, lastName, email, role):
        """
        Method to Create new User having the details provided(arguments). Bypasses an error after creating user to verify.
        """
        self.waitForElement(locator=self._createUserBtn, locatorType="xpath")
        self.elementClick(locator=self._createUserBtn, locatorType="xpath")
        self.waitForElement(locator=self._createUser_firstName)
        self.sendKeys(firstName, locator=self._createUser_firstName)
        self.sendKeys(lastName, locator=self._createUser_lastName)
        self.sendKeys(email, locator=self._createUser_email)
        self.selectBy(by="text", data="User", locator=self._createUser_role)
        pp.time.sleep(2)
        self.elementClick(locator=self._createUser_addUserBtn, locatorType="xpath")
        # Bypassing error code
        self.driver.back()
        self.driver.refresh()

    def verifyUser(self, email):
        """
        Verify User Creation
        """
        self.waitForElement(locator=self._verifyUserEmail.format(email), locatorType="xpath")
        result = self.isElementPresent(locator=self._verifyUserEmail.format(email), locatorType="xpath")
        self.log.info("Verify User Creation result: " + str(result))
        return result

    def clickViewProfile(self):
        """
        Click on View Profile button for a user
        """
        self.waitForElement(locator=self._viewProfileBtn, locatorType="xpath")
        element = self.getElementList(locator=self._viewProfileBtn, locatorType="xpath")
        self.elementClick(element=element[0])

    def verifyViewProfile(self):
        """
        Verify Profile page display
        """
        self.waitForElement(locator=self._viewProfileImg, locatorType="xpath")
        result = self.isElementPresent(locator=self._viewProfileImg, locatorType="xpath")
        self.log.info("Verify View Profile result: " + str(result))
        return result

    def clickTeam(self):
        """
        Click on Team details box
        """
        # self.webScroll(direction="down")
        self.scrollIntoView(locator=self._userProfile_team, locatorType="xpath")
        self.waitForElement(locator=self._userProfile_team, locatorType="xpath")
        self.elementClick(locator=self._userProfile_team, locatorType="xpath")
        pp.time.sleep(2)

    def verifyTeamOpenClose(self):
        """
        Verify Team details Expand/Collapse window status
        """
        element = self.getElement(locator=self._userProfile_membersTable)
        value = self.getAttribute(attribute="class", element=element)
        if "show" in value:
            self.log.info("Verify Team details window result: " + str(True))
            return True
        else:
            self.log.info("Verify Team details window result: " + str(False))
            return False

    def clickDetails(self):
        """
        Click on details button on team details window
        """
        self.waitForElement(locator=self._userProfile_detailsBtn, locatorType="xpath")
        element = self.getElementList(locator=self._userProfile_detailsBtn, locatorType="xpath")
        self.elementClick(element=element[0])
        pp.time.sleep(2)



