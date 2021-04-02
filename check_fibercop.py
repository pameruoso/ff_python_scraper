import os
import time
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('log-level=3')
driver = Edge(r"msedgedriver.exe", options = edge_options)

print("Inserisci la città:")
citta = input().upper()
print("Inserisci la via:")
indirizzo = input().upper()
print("Inserisci il numero civico")
civico = input().upper()

print("Controllo disponibilita Fibra Fibercop su" + indirizzo)
driver.get('https://www.fibercop.it')

ff_citta = driver.find_element_by_id('ff-citta')
time.sleep(3)
ff_citta.send_keys(citta)
ff_citta.send_keys(Keys.RETURN)
citta_xpath = '//li[text()='+'\"'+ citta + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, citta_xpath))).click()

ff_indirizzo = driver.find_element_by_id('ff-indirizzo')
ff_indirizzo.send_keys(indirizzo)
ff_indirizzo.send_keys(Keys.RETURN)
ind_xpath = '//li[text()='+'\"'+ indirizzo + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ind_xpath))).click()

ff_civico = driver.find_element_by_id('ff-civico')
ff_civico.send_keys(civico)
ff_civico.send_keys(Keys.RETURN)
civ_xpath = '//li[text()='+'\"'+ civico + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, civ_xpath))).click()


ff_submit = driver.find_element_by_id('ff-submit')
ff_submit.submit()

time.sleep(7)
result = driver.find_element_by_xpath('//meta[@property="og:title"]').get_attribute("content")
print (result)
driver.close()
quit()
