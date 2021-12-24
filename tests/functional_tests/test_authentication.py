from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestAuthentication:
    def test_showSummary(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME, 'email').send_keys("kate@shelifts.co.uk")
        browser.find_element(By.TAG_NAME, 'button').click()
        assert browser.title == "Summary | GUDLFT Registration"
        assert browser.current_url == "http://127.0.0.1:5000/showSummary"
        browser.close()

    def test_logout_route(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME, 'email').send_keys("kate@shelifts.co.uk")
        browser.find_element(By.TAG_NAME, 'button').click()
        browser.find_element(By.CLASS_NAME, "logout").click()
        assert browser.title == "GUDLFT Registration"
        assert browser.current_url == "http://127.0.0.1:5000/"
        browser.close()
