# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage

class CategoryPage(BasePage):
    def __init__(self, driver, name):
        self.driver=driver
        self.name=name

    def at(self):
        assert (self.name in self.driver.title)

    def productTable(self):
        return self.driver.find_element_by_xpath("//div[@data-role='product-list']/div")

    def productLines(self):
        return self.productTable().find_elements_by_xpath("//div[@class='product']")

    def changeSorting(self):
        self.driver.find_element_by_xpath("//div[@class='dropdown' and @data-ordering-key='order']/button").click() # открыть выпадающий список
        self.driver.find_element_by_xpath(u"//div[@class='dropdown open' and @data-ordering-key='order']/ul/li/a[ . ='По убыванию цены']").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@data-role='product-list']/div")))

class ProductLine():
    def __init__(self,webelement):
        self.webelement=webelement

    def productTitle(self):
        return self.webelement.find_element_by_xpath("./div/div[@class='caption']/div[@class='item-name']/a").text

    def productPrice(self):
        return float(self.webelement.find_element_by_xpath("./div/div[@class='item-price']/div/div/div/span[@data-of='price-total']").get_attribute("data-value"))
