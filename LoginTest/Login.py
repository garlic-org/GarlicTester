from selenium import webdriver
import os
import time

#Time waiting for page
waiting_for_page = 10

#ক্রম ডাইভার কাজ করানো
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("K:\Project\Python\GarlicTester\chromedriver.exe", chrome_options=options)

#ওয়েব সাইটে যা্ওয়া
driver.get("https://marketplace.garlic.marvelous-tech.com/")

'''
#লগিন করবো এন ভায়রনমেন্ট ভেরিয়েবল দিয়ে
# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)
#লিস্টে যাওয়ার কোড শুরু
url = "https://www.linkedin.com/sales/lists/people/6706420163950055424?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)
'''