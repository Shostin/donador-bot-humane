import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nombres = ["Juan", "Ana", "Luis", "María", "Carlos", "Lucía", "Pedro", "Elena", "Diego", "Sofía"]
apellidos = ["Pérez", "Gómez", "Rodríguez", "López", "Hernández", "Martínez"]
nombre = random.choice(nombres)
apellido = random.choice(apellidos)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://secure.humaneworld.org/page/161274/donate/1?ea.tracking.id=web_topnav")

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.NAME, "donor.first_name")))

driver.find_element(By.NAME, "donor.first_name").send_keys(nombre)
driver.find_element(By.NAME, "donor.last_name").send_keys(apellido)
driver.find_element(By.NAME, "donor.email_address").send_keys(f"{nombre.lower()}.{apellido.lower()}@example.com")
driver.find_element(By.NAME, "donor.address1").send_keys("Calle Falsa 123")
driver.find_element(By.NAME, "donor.city").send_keys("Ciudad")
driver.find_element(By.NAME, "donor.postal_code").send_keys("12345")

other_amount = driver.find_element(By.ID, "other-amount-input")
other_amount.clear()
other_amount.send_keys("5")

time.sleep(2)

iframe_card = driver.find_element(By.CSS_SELECTOR, "iframe[name*='card-number']")
driver.switch_to.frame(iframe_card)
driver.find_element(By.NAME, "cardnumber").send_keys("1234123412341234")
driver.switch_to.default_content()

iframe_exp = driver.find_element(By.CSS_SELECTOR, "iframe[name*='card-expiry']")
driver.switch_to.frame(iframe_exp)
driver.find_element(By.NAME, "exp-date").send_keys("0129")
driver.switch_to.default_content()

iframe_cvc = driver.find_element(By.CSS_SELECTOR, "iframe[name*='card-cvc']")
driver.switch_to.frame(iframe_cvc)
driver.find_element(By.NAME, "cvc").send_keys("123")
driver.switch_to.default_content()

print(f"Formulario listo con nombre: {nombre} {apellido} y monto: $5")
input("Presiona ENTER para cerrar el navegador...")
driver.quit()
