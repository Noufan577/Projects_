from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/")


element=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')

element.send_keys("Messi images")

element.send_keys(Keys.ENTER)

time.sleep(5) 

bot_tick=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")

bot_tick.click()




#driver.quit()