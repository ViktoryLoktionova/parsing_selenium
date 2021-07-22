import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # ждем пять секунд
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver') # текст запроса в гугл
search_box.submit() #клик мышки или энтера

wait = WebDriverWait(driver, 10)
first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>span")))
print(first_result.get_attribute("textContent"))

time.sleep(5) # ждем пять секунд и завершаем работу
driver.quit()