"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.
You shall follow all the terms of the MIT License (./LICENSE).
"""


# ----- Requires: selenium == 4.7.2 -----
# ----- Requires: webdriver-manager == 3.8.5 -----

from time import sleep

# Import all selenium and webdriver tools
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

microsoft_authentication_link = "https://go.microsoft.com/fwlink/p/?linkid=873020"
email = ""
password = ""

MSG = "ASJKDHFJKH"

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get(microsoft_authentication_link)

sleep(2)

print("Clicking other account")
other_account = driver.find_element_by_xpath("//div[3]/div/div/div[2]")
other_account.click()

sleep(0.5)

email_input = driver.find_element_by_id("i0116")
email_input.send_keys(email)

click_next = driver.find_element_by_id("idSIButton9")
click_next.click()

sleep(0.5)

email_input = driver.find_element_by_id("i0118")
email_input.send_keys(password)

click_next = driver.find_element_by_id("idSIButton9")
click_next.click()

sleep(0.5)

click_next = driver.find_element_by_id("idBtn_Back")
click_next.click()

sleep(6)

click_chat = driver.find_element_by_css_selector(".icons-chat")
click_chat.click()

sleep(2)

# Test user
click_user = driver.find_element_by_css_selector(".content > div:nth-child(2) > .recipient-group-list-item > .cle-item")
click_user.click()

sleep(5)


driver.execute_script("window.scrollTo(0,0)")

driver.execute_script('document.querySelector(".ck-placeholder").innerHTML = "TEST";')

sleep(10)


driver.close()
driver.quit()
