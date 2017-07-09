# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from BasePage import BasePage

class DNSMainPage(BasePage):
    def go(self):
        self.driver.get("http://www.dns-shop.ru/")
        assert "DNS" in self.driver.title

    def FirstLevelMenu(self,name):
        link=self.driver.find_elements_by_xpath("//a/span[. = '" +name+ "']")[1]        
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()

    def SecondLevelMenu(self,name):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[. = '" +name+ "']")))
        element.click()
