from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time


class TestPurchasePlaces:
    def test_purchase_places_futur_competition(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME,'email').send_keys("kate@shelifts.co.uk")
        browser.find_element(By.TAG_NAME,'button').click()
        browser.find_elements(By.LINK_TEXT,"Book Places")[2].click()
        remaining_places = browser.find_element(By.CLASS_NAME,"places").text
        assert "Places available: 21" in remaining_places
        browser.find_element(By.NAME,"places").send_keys("1")
        browser.find_element(By.TAG_NAME,"button").click()
        assert "Summary | GUDLFT Registration" in browser.title
        competition_infos = browser.find_elements(By.CLASS_NAME,"competition_list")[2].text
        assert "Number of Places: 20" in competition_infos
        browser.close()

    def test_purchase_places_past_competition(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME,'email').send_keys("kate@shelifts.co.uk")
        browser.find_element(By.TAG_NAME,'button').click()
        browser.find_elements(By.LINK_TEXT,"Book Places")[0].click()
        error_message = "You cannot book places for an already past competition"
        assert error_message in browser.find_element(By.CLASS_NAME,"error").text
        browser.close()

    def test_purchase_more_places_than_club_points(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME,'email').send_keys("admin@irontemple.com")
        browser.find_element(By.TAG_NAME,'button').click()
        browser.find_elements(By.LINK_TEXT,"Book Places")[2].click()
        browser.find_element(By.NAME,"places").send_keys("6")
        browser.find_element(By.TAG_NAME,"button").click()
        error = "You cannot book more places than your club current number of points"
        assert error in browser.find_element(By.CLASS_NAME,'places_error').text
        assert "Booking for" in browser.title
        browser.close()

    def test_purchase_more_than_12_places(self):
        browser = webdriver.Firefox(service=Service("tests/functional_tests/geckodriver.exe"))
        browser.get("http://127.0.0.1:5000/")
        browser.find_element(By.NAME,'email').send_keys("john@simplylift.co")
        browser.find_element(By.TAG_NAME,'button').click()
        browser.find_elements(By.LINK_TEXT,"Book Places")[2].click()
        browser.find_element(By.NAME,"places").send_keys("13")
        browser.find_element(By.TAG_NAME,"button").click()
        error = "You cannot book more than 12 places for each competition"
        assert error in browser.find_element(By.CLASS_NAME,'places_error').text
        assert "Booking for" in browser.title
        browser.close()