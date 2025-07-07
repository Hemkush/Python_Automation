from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

# define url
url = "https://the-internet.herokuapp.com/drag_and_drop"

# instantiate webdriver and open a chrome browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# maximize browser window
driver.maximize_window()
# load the webpage
driver.get(url)

# find the source element (Box A)
source_element = driver.find_element(By.XPATH, '//*[@id="column-a"]')
# find the destination element (Box B)
destination_element = driver.find_element(By.XPATH, '//*[@id="column-b"]')
# create an instance of ActionChains
actions = ActionChains(driver)
# drag and drop the source element to the destination element
actions.drag_and_drop(source_element, destination_element).perform()

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver  
driver.quit()