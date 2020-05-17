# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# # driver.set_window_position(0, -1000)
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://learn.letskodeit.com/p/practice")
# bmwRadioBtn = driver.find_element_by_xpath("(//input[@id='bmwradio'])")
# bmwRadioBtn.click()
# time.sleep(3)
# benzRadioBtn = driver.find_element_by_xpath("(//input[@id='benzradio'])")
# benzRadioBtn.click()
# print("Radio is selected? " + str(bmwRadioBtn.is_selected()))
# print("Radio is selected? " + str(benzRadioBtn.is_selected()))