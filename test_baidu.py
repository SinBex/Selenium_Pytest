#-*-coding=utf-8
from selenium import webdriver
import os,time
import pytest
from Selenium_loadbaidupan import loadbaidupan

class Testbaidu:
    def setup_class(self):
        test = loadbaidupan()
        test.load()
        self.test = test
        self.verificationErrors = []

    def teardown_class(self):
        test = self.test
        test.close()

    def test_file_up_delete(self):
        test = self.test
        test.fileup()
        test.filedete()

    def test_searchfile(self):
        test = self.test
        test.searchfile()
        test.download()

    def test_mousemove(self):
        test = self.test
        test.mousemove()
        test.personalInfor()

if __name__ == '__main__':
    pytest.main()

