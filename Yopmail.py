from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.common.by import By
import selenium

usr=input('Enter Email:')
driver = webdriver.Chrome()
element = driver.get('http://www.yopmail.com/' + usr)
print ("Opened yopmail")
sleep(1)
try:
    #element = driver.find_elements_by_xpath("//*[@id='m1']/div/a/span[1]/span[2]")
    element = driver.find_element_by_class_name("whc")
    print(element.text)
except:
    print("Algo salio mal")

driver.quit()
print("Finished")
input("Press a key to exit")
