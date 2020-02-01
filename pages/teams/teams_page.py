"""
All the Teams page related methods will be present in this class
"""
from pages import page_package as pp


class Teams(pp.BasePage):

    log = pp.cl.customLogger(pp.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _navBar_teams = "//a[contains(text(),'Teams')]"
    _dashboardBtn = "//a[contains(text(),'Dash')]"
    _verifyDashboardText = "//h5[contains(text(),'Recently Assigned Tickets')]"
    _createTeamBtn = "//button[@data-target='#modalTeamForm']"
    _createTeam_teamName = "companyTeamDTO_Name"
    _createTeam_addTeamBtn = "//div[@id='modalTeamForm']//button[contains(text(),'Add Team')]"
    _verifyTeamName = "//td[contains(text(),'{}')]"
    _createTeam_close = "modalTeamForm"
    _addTeamUsersBtn = "//button[@data-target='#modalTeamUserForm']"
    _addTeamUsers_selectTeam = "teamMemberDTO_CompanyTeamId"
    _addTeamUsers_selectMember = "Member_list"
    _addTeamUsers_addTeamBtn = "//div[@id='modalTeamUserForm']//button[contains(text(),'Add Team')]"
    _verifyTeamUser_totalUsers = "//td[contains(text(),'{}')]/following-sibling::td[1]"
    _verifyMembersTable = "//h5[contains(text(),'All Members in Team')]"
    _viewMembersBtn = "//a[@name='{}']"
    _memberDetails_viewProfileBtn = "//b[contains(text(),'{}')]/parent::td/following-sibling::td[3]//a"
    _verifyViewProfile = "//h3[contains(text(),'{}')]"

    def gotoTeams(self):
        """
        Method to Click on Teams Link and go to Teams Page
        """
        self.elementClick(locator=self._navBar_teams, locatorType="xpath")

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
        self.log.info("Verify Dashboard result: " + str(result))
        return result

    def createTeam(self, name):
        """
        Method to Create new Team having the details provided(arguments).
        """
        self.waitForElement(locator=self._createTeamBtn, locatorType="xpath")
        self.elementClick(locator=self._createTeamBtn, locatorType="xpath")
        self.sendKeys(data=name, locator=self._createTeam_teamName)
        self.elementClick(locator=self._createTeam_addTeamBtn, locatorType="xpath")

    def verifyTeam(self, name):
        """
        Verify Team Creation
        """
        self.waitForElement(locator=self._verifyTeamName.format(name), locatorType="xpath")
        result = self.isElementPresent(locator=self._verifyTeamName.format(name), locatorType="xpath")
        self.log.info("Verify Team Creation result: " + str(result))
        return result

    def verifyInvalidTeam(self):
        """
        Verify Invalid Team Creation. Produces an error and verifies error text from alert box.
        """
        self.waitForElement(locator=self._createTeamBtn, locatorType="xpath")
        self.elementClick(locator=self._createTeamBtn, locatorType="xpath")
        self.elementClick(locator=self._createTeam_addTeamBtn, locatorType="xpath")
        alert = self.waitForAlert()
        alertText = alert.text
        if alertText == "Team Name Cannot Be Blank":
            alert.accept()
            self.elementClick(locator=self._createTeam_close)
            self.log.info("Verify Invalid Team Creation alert box result: " + str(True))
            return True
        else:
            self.log.info("Verify Invalid Team Creation alert box result: " + str(False))
            return False

    def addTeamUsers(self, team, member1, member2):
        """
        Add Users to a team using the provided values(parameters).
        :param team: Team name
        :param member: Member name
        """
        self.waitForElement(locator=self._addTeamUsersBtn, locatorType="xpath")
        self.elementClick(locator=self._addTeamUsersBtn, locatorType="xpath")
        self.waitForElement(locator=self._addTeamUsers_selectTeam)
        self.selectBy(by="text", data=team, locator=self._addTeamUsers_selectTeam)
        self.selectBy(by="text", data=member1, locator=self._addTeamUsers_selectMember)
        self.selectBy(by="text", data=member2, locator=self._addTeamUsers_selectMember)
        self.elementClick(locator=self._addTeamUsers_addTeamBtn, locatorType="xpath")

    def verifyAddTeamUsers(self, teamName):
        """
        Verifies for users added to a team.
        :param teamName: Team name
        """
        self.waitForElement(locator=self._verifyTeamUser_totalUsers.format(teamName), locatorType="xpath")
        totalUsers = self.getText(locator=self._verifyTeamUser_totalUsers.format(teamName), locatorType="xpath")
        if int(totalUsers) > 0:
            self.log.info("Verify Add team users result: " + str(True))
            return True
        else:
            self.log.info("Verify Add team users result: " + str(False))
            return False

    def clickViewMembers(self, teamName):
        """
        Click on View Members button
        :param teamName: Team Name
        """
        self.waitForElement(locator=self._viewMembersBtn.format(teamName), locatorType="xpath")
        self.elementClick(locator=self._viewMembersBtn.format(teamName), locatorType="xpath")

    def verifyMemberTable(self):
        """
        Verify Member table list display.
        """
        result = self.isElementDisplayed(locator=self._verifyMembersTable, locatorType="xpath")
        self.log.info("Verify Team member display result: " + str(result))
        return result

    def clickViewProfile(self, userName):
        """
        Click on view profile button in team display window
        :param userName: User's name to be selected
        """
        self.waitForElement(locator=self._memberDetails_viewProfileBtn.format(userName), locatorType="xpath")
        self.elementClick(locator=self._memberDetails_viewProfileBtn.format(userName), locatorType="xpath")

    def verifyViewProfile(self, userName):
        """
        Verify View profile for the selected user
        :param userName: User name
        """
        self.waitForElement(locator=self._verifyViewProfile.format(userName), locatorType="xpath")
        result = self.isElementPresent(locator=self._verifyViewProfile.format(userName), locatorType="xpath")
        self.log.info("Verify View Profile result: " + str(result))
        return result
