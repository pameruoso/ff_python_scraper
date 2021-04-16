import time
#from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

edge_options = EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('log-level=3')
driver = Edge(r"msedgedriver.exe", options = edge_options)

print("Inserisci la città:")
citta = input()
print("Inserisci la via:")
via = input()
print("Inserisci il numero civico")
civico = input()

print("####################################################")
print("Controllo disponibilità Fibra FF su " + via)
driver.get('https://flashfiber.it')

ff_citta = driver.find_element_by_id('ff-citta')
ff_citta.send_keys(citta)
time.sleep(2)

ff_indirizzo = driver.find_element_by_id('ff-indirizzo')
ff_indirizzo.send_keys(via)
time.sleep(2)

ff_civico = driver.find_element_by_id('ff-civico')
ff_civico.send_keys(civico)
time.sleep(2)

ff_submit = driver.find_element_by_id('ff-submit')
ff_submit.submit()
time.sleep(5)

result = driver.find_elements_by_class_name('wpb_wrapper')
print(result[0].text)
print("####################################################")
driver.quit()
quit()
