from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import StaleElementReferenceException
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(EdgeChromiumDriverManager().install())#Specify Browser
driver.get("https://www.bing.com") # Insert Desired URL
print("Application Title is ",driver.title)
print("Application urlis ",driver.current_url)
searchBar = driver.find_element(By.NAME, 'q') #Locating the Search bar

searchBar.send_keys("Bleak")
searchBar.send_keys(Keys.RETURN)
print("User searched")
print("Application Title is ",driver.title)
time.sleep(1)
searchBar.send_keys(Keys.CLEAR)
#Code to interract and find search bar on Google
searchBar.send_keys("Google")
searchBar.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 20)
google_link = wait.until(expected_condiions.visibility_of_element_located((By.LINK_TEXT, "Google"))) #Explicitly waiting for Googlelink to appear pn page.
google_link.click()

##driver.close()