from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class internetSpeedTwitterBot():
    def __init__(self,DRIVER_PATH):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.up = Keys.UP
        self.down = Keys.DOWN
    def getInternetProvider(self):
        self.driver.get(url="https://www.speedtest.net/")
        goBut = self.driver.find_element_by_css_selector(".js-start-test")
        goBut.click()
        time.sleep(60)
        downSpeed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upSpeed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        speeds=[float(downSpeed.text),float(upSpeed.text)]
        return speeds
    def tweetAtProvider(self,EMAIL ,USER,PASS,MESSAGE):
        self.driver.get(url="https://twitter.com/login")
        time.sleep(10)
        usernameInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        usernameInput.send_keys(EMAIL)
        # usernameInput.send_keys(Keys.ENTER)
        passInput = self.driver.find_element_by_name("session[password]")
        passInput.send_keys(PASS)
        passInput.send_keys(Keys.ENTER)


        try:
            btnInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            btnInput.click()
        except:
            time.sleep(10)
            usernameInput = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            usernameInput.send_keys(USER)
            # usernameInput.send_keys(Keys.ENTER)
            passInput = self.driver.find_element_by_name("session[password]")
            passInput.send_keys(PASS)
            passInput.send_keys(Keys.ENTER)
            time.sleep(10)
            btnInput = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            btnInput.click()
        finally:
            time.sleep(3)
            textinput = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
            textinput.clear()
            textinput.send_keys(MESSAGE)
            tweetBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div')
            tweetBtn.click()