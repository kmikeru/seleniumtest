# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
from DNSMainPage import DNSMainPage
from CategoryPage import CategoryPage,ProductLine

class DNSSortingTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("/usr/bin/chromedriver")

    def test_category_page_sorting1(self):
        self.category_page_sorting(u"Автотовары",u"Видеорегистраторы")

    def test_category_page_sorting2(self):
        self.category_page_sorting(u"Аудиотехника",u"Колонки")

    def category_page_sorting(self,categoryname,subcategoryname):
        mainPage=DNSMainPage(self.driver)
        mainPage.go()
        mainPage.FirstLevelMenu(categoryname)        
        sleep(10)
        mainPage.SecondLevelMenu(subcategoryname)
        categoryPage=CategoryPage(self.driver,subcategoryname)
        categoryPage.at()
        assert len(categoryPage.productLines()) > 2

        prodFirst=ProductLine(categoryPage.productLines()[0])
        prodLast=ProductLine(categoryPage.productLines()[-1])
        print prodFirst.productTitle()+' '+str(prodFirst.productPrice())
        print prodLast.productTitle()+' '+str(prodLast.productPrice())
        assert (prodLast.productPrice() > prodFirst.productPrice() )

        categoryPage.changeSorting()

        prodFirstAfterSort=ProductLine(categoryPage.productLines()[0])
        prodLastAfterSort=ProductLine(categoryPage.productLines()[-1])
        print prodFirstAfterSort.productTitle()+' '+str(prodFirstAfterSort.productPrice())
        print prodLastAfterSort.productTitle()+' '+str(prodLastAfterSort.productPrice())
        assert (prodLastAfterSort.productPrice() < prodFirstAfterSort.productPrice() )

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
