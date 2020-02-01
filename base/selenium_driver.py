from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../reporting/screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        """
        returns title of the current web page
        """
        return self.driver.title

    def getByType(self, locatorType):
        """
        Determines and returns the By type
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        """
        Finds and returns an element using the provided locator and type
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element(s) is/are present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        """
        Wait for an element for 'timeout' number of seconds and check after every 'pollFrequency' interval
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def waitForAlert(self, timeout=10, pollFrequency=0.5):
        """
        Wait for an Alert for 'timeout' number of seconds and check after every 'pollFrequency' interval
        """
        alert = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for alert")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            alert = wait.until(EC.alert_is_present())
            self.log.info("Alert appeared on the web page")
        except:
            self.log.info("Alert did not appear on the web page")
            print_stack()
        return alert

    def webScroll(self, direction="up"):
        """
        For scrolling up and down the webpage
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

        if direction == "right":
            # Scroll Right
            self.driver.execute_script("window.scrollBy(1000, 0);")

        if direction == "left":
            # Scroll Left
            self.driver.execute_script("window.scrollBy(-1000, 0);")

        if direction == "infinite":
            # Infinite Page Scroll
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scrollIntoView(self, locator="", locatorType="id", element=None, native=False):
        """
        Scroll down the web page by the visibility of the element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if native:
                location = element.location_once_scrolled_into_view
            else:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            self.log.info("Scrolled to the element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot scroll to the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()


    def switchFrame(self, locator="", locatorType="id", element=None):
        """
        Switch/move into an iFrame in the DOM
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("iFrame found with locator: " + locator +
                              " locatorType: " + locatorType)
                self.driver.switch_to.frame(element)
            else:
                self.log.info("iFrame not found with locator: " + locator +
                              " locatorType: " + locatorType)
        except:
            self.log.info("iFrame not found")
            print_stack()

    def getURL(self, url):
        """
        Go to url
        """
        self.driver.get(url)

    def selectBy(self, by, data, locator="", locatorType="id", element=None):
        """
        Uses selenium Select class to select an item from a dropdown
        item: item to be selected
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +
                              " locatorType: " + locatorType)
                by = by.lower()
                select = Select(element)
                if by == "value":
                    select.select_by_value(data)
                elif by == "index":
                    select.select_by_index(data)
                elif by == "text":
                    select.select_by_visible_text(data)
                else:
                    self.log.info("by type " + by + " not correct/supported")
                self.log.info("Selected value " + data + " from dropdown")
            else:
                self.log.info("Element not found with locator: " + locator +
                              " locatorType: " + locatorType)
        except:
            self.log.info("Cannot select item by value")
            print_stack()

    def getAttribute(self, attribute, locator="", locatorType="id", element=None):
        """
        Get Attribute value of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +
                              " locatorType: " + locatorType)
                value = element.get_attribute(attribute)
                self.log.info("Value of attribute " + attribute + " : " + value)
                return value
            else:
                self.log.info("Element not found with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Failed to get value of attribute " + attribute)
            print_stack()
            return False
