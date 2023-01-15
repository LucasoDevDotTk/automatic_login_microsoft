"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.
You shall follow all the terms of the MIT License (./LICENSE).
"""


# ----- Requires: selenium == 4.7.2 -----
# ----- Requires: webdriver-manager == 3.8.5 -----

from time import sleep

# Import all selenium and webdriver tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Function for login with Microsoft Authentication portal when cookies with other accounts is shown
def login_cookies(email, password, microsoft_authentication_link):

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(microsoft_authentication_link)

    sleep(2)
    print("Clicking other account")
    other_account = driver.find_element_by_xpath("//div[3]/div/div/div[2]")
    other_account.click()

    sleep(1)

    email_input = driver.find_element_by_id("i0116")
    email_input.send_keys(email)

    click_next = driver.find_element_by_id("idSIButton9")
    click_next.click()

    sleep(1)

    email_input = driver.find_element_by_id("i0118")
    email_input.send_keys(password)

    click_next = driver.find_element_by_id("idSIButton9")
    click_next.click()

    sleep(1)

    click_next = driver.find_element_by_id("idBtn_Back")
    click_next.click()

    return driver


# Function for login of Microsoft Authentication portal when no accounts have been collected.
def login(email, password, microsoft_authentication_link):

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(microsoft_authentication_link)

    sleep(1)

    email_input = driver.find_element_by_id("i0116")
    email_input.send_keys(email)

    click_next = driver.find_element_by_id("idSIButton9")
    click_next.click()

    sleep(1)

    email_input = driver.find_element_by_id("i0118")
    email_input.send_keys(password)

    click_next = driver.find_element_by_id("idSIButton9")
    click_next.click()

    sleep(1)

    click_next = driver.find_element_by_id("idBtn_Back")
    click_next.click()

    return driver