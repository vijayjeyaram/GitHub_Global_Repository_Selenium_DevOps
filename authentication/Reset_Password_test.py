import time

import pytest
from selenium import webdriver
import logging

from selenium.webdriver import DesiredCapabilities

logging.basicConfig(
    filename="../Logs/Authentication.log",
    format='%(asctime)s: %(levelname)s: %(message)s',
    level=logging.DEBUG)


class Test_Reset_Password:
    driver = None

    @pytest.yield_fixture()
    def startup(self):
        self.invoke_browser(self)
        yield
        self.close_browser(self)

    @staticmethod
    def invoke_browser(self):

        deployment_Type = "cloud"
        deployment_Environment = "osx"
        browser = "chrome"
        remote_Machine = 'http://localhost:4444/wd/hub'

        logging.info(
            "Started:Internet Banking Reset Password Flow. FileName: Rest_Password_test.py, ClassName:Test_Reset_Password, TestName:test_Rest_Password")

        if deployment_Type == "cloud":
            if deployment_Environment == "osx":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Firefox Browser has been launched.")

            elif deployment_Environment == "linux":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Firefox Browser has been launched.")

            else:  # windows
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Firefox Browser has been launched.")

        else:  # on premise
            if deployment_Environment == "osx":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver")
                    logging.debug("On Premise-OSX-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver")
                    logging.debug("On Premise-OSX-Firefox Browser has been launched.")

            elif deployment_Environment == "linux":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver")
                    logging.debug("On Premise-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver")
                    # logging.debug("On Premise-Linux-Firefox Browser has been launched.")

            else:  # windows
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver.exe")
                    logging.debug("On Premise-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver.exe")
                    logging.debug("On Premise-Windows-Firefox Browser has been launched.")

        self.driver.maximize_window()
        self.driver.get("https://mobile.qa.cubusbank.com/Mobile/Authentication/SignIn.aspx")
        logging.debug("Internet Banking URL has been passed to the browser.")
        time.sleep(5)

    @staticmethod
    def close_browser(self):
        self.driver.close()
        logging.info(
            "Started:Internet Banking Reset Password Flow. FileName: Rest_Password_test.py, ClassName:Test_Reset_Password, TestName:test_Rest_Password")

    def test_Rest_Password(self, startup):

        try:
            self.driver.find_element_by_xpath("//a[@id='ctl00_CPHSectionContent_Link_ForgotPassword']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//input[@id='ctl00_CPHSectionContent_Textbox_Username']").send_keys(
                "Test24")
            self.driver.find_element_by_xpath("//input[@id='ctl00_CPHSectionContent_Textbox_SecurityCode']").send_keys(
                "Valid Captcha")
            self.driver.find_element_by_xpath("//input[@id='ctl00_CPHSectionContent_Button_Submit']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//input[@id='ctl00_CPHSectionContent_Textbox_NewPassword']").send_keys(
                "Test24!")
            self.driver.find_element_by_xpath("//input[@id='ctl00_CPHSectionContent_Textbox_RetPassword']").send_keys(
                "Test24!")
            time.sleep(5)

        except Exception as e:
            logging.error("ERROR: Issue in --test_Rest_Password()-- Method.", e)