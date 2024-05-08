from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bing.com")
print("Application Title is ",driver.title)
print("Application urlis ",driver.current_url)
driver.implicitly_wait(10000)
driver.quit()