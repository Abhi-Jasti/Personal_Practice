from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome() #Specify Browser
driver.maximize_window() 
driver.get("https://www.bing.com") # Insert Desired URL
print("Application Title is ",driver.title)
print("Application urlis ",driver.current_url)
searchBar = driver.find_element(By.NAME, 'q') #Locating the Search bar
print(type(searchBar))
searchBar.send_keys("Bleak")
searchBar.send_keys(Keys.RETURN)
print("User searched")
print("Application Title is ",driver.title)

driver.close()