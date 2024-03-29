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
citta = ""
while True:
    citta = input().upper()
    if citta == "":
        print("La città è un campo obbligatorio")
    else:
        break

print("Inserisci la via:")
indirizzo = ""
while True:
    indirizzo = input().upper()
    if indirizzo == "":
        print("La via è un campo obbligatorio")
    else:
        break

print("Inserisci il numero civico:")
civico = ""
while True:
    civico = input().upper()
    if civico == "":
        print("Il numero civico è un campo obbligatorio")
    else:
        break

print("Controllo disponibilità Fibra Fibercop su " + indirizzo + ", " + civico + " - " + citta)
driver.get('https://www.fibercop.it')

time.sleep(2)
ff_citta = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ff-citta')))
ff_citta.send_keys(citta)
citta_xpath = '//li[text()='+'\"'+ citta + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, citta_xpath))).click()

ff_indirizzo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ff-indirizzo')))
ff_indirizzo.send_keys(indirizzo)
ind_xpath = '//li[text()='+'\"'+ indirizzo + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ind_xpath))).click()

ff_civico = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ff-civico')))
ff_civico.send_keys(civico)
civ_xpath = '//li[text()='+'\"'+ civico + '\"'+']'
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, civ_xpath))).click()


ff_submit = driver.find_element_by_id('ff-submit')
ff_submit.submit()

result = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Verifica un altro indirizzo"]')))
result = driver.find_element_by_xpath('//meta[@property="og:title"]').get_attribute("content")
print (result)
driver.quit()
quit()
