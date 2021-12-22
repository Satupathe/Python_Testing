from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time


class TestClubsList:
    def test_display_clubs_list(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME,'email').send_keys("kate@shelifts.co.uk")
        browser.find_element(By.TAG_NAME,'button').click()
        browser.find_element(By.CLASS_NAME,"club_list").click()
        assert browser.title == "Summary | GUDLFT clubs list"
        assert browser.current_url == "http://127.0.0.1:5000/clubsList"
        welcome_text = "Here, you can see and follow each club remaining points"
        assert welcome_text in browser.find_element(By.TAG_NAME,"p").text
        browser.close()