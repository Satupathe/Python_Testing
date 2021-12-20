from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import server
from server import showSummary, clubs, app, book, getClubsList
from flask import Flask, template_rendered, url_for, request, current_app
import time


class TestAuthentication:
    def test_showSummary(self):
        self.browser = webdriver.Firefox("tests/functional_tests/geckodriver.exe")
        self.browser.get("http://http://127.0.0.1:5000/")
        self.browser.find_element_by_name('email').send_keys("kate@shelifts.co.uk")
        self.browser.find_element_by_tag_name('button').click()
        time.sleep(3)
        assert self.browser.title == "Summary | GUDLFT Registration"
        assert self.browser.current_url == "http://127.0.0.1:5000/showSummary"
        time.sleep(3)
        self.browser.close()