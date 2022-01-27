from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get('https://wa.me/5531996949218')

alert = driver.switch_to.alert()
alert.dismiss()
