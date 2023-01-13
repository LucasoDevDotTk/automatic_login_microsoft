"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.
You shall follow all the terms of the MIT License (./LICENSE).
"""


# ----- Requires: selenium == 4.7.2 -----
# ----- Requires: webdriver-manager == 3.8.5 -----
# ----- Requires: msedge-selenium-tools -----

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions


driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

options = EdgeOptions()
options.use_chromium = True
options.add_argument("-inprivate")

driver.set_window_size(1920,1080)

driver.get('https://go.microsoft.com/fwlink/p/?linkid=873020&clcid=0x409&culture=en-us&country=us')

sleep(10)

driver.close()
driver.quit()
