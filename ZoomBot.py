from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://zoom.us/")

join = driver.find_element_by_id("btnJoinMeeting")
join.click()

meetingid = driver.find_element_by_id("join-confno")
meetingid.send_keys("") #put your meeting id/link here between the quotes.

meetingidjoin = driver.find_element_by_id("btnSubmit")
meetingidjoin.click()