from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime

options = Options()
options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica
options.add_argument("--no-sandbox") 
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



driver.get("https://cordoba.redesclimaticas.com/next/login?&next=/")
sleep(3)


username_input = driver.find_element(By.XPATH, '//*[@id="field-:r2:"]')
password_input = driver.find_element(By.XPATH, '//*[@id="field-:r3:"]')

username_input.send_keys("Eilchz14")
password_input.send_keys("Abii2021")
sleep(3)

login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/form/div[4]/button')
login_button.click()
sleep(8)

driver.get("https://cordoba.redesclimaticas.com/next/station?s=30405")
sleep(5)

# Extracción de datos
temperature_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[5]/div/div/div[2]/div[1]/strong[1]')
humidity_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[12]/div/div/div[2]/div[1]/strong')
rain_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]/strong')
raini_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]/p')
rainw_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[3]/p[1]/strong')
rainm_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[3]/p[2]/strong')
raina_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[3]/p[3]/strong')
radiation_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[7]/div/div/div[2]/div[1]/strong')
wind_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/strong')
rocio_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[6]/div/div/div[3]/p[3]/strong')
presion_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[9]/div/div/div[2]/div[1]/strong')

temperature = temperature_element.text
humidity = humidity_element.text
rain = rain_element.text
raini = raini_element.text
rainw = rainw_element.text
rainm = rainm_element.text
raina = raina_element.text
radiation = radiation_element.text
wind = wind_element.text
rocio = rocio_element.text
presion = presion_element.text

# Obtener fecha y hora actual
now = datetime.now()
fecha_hora_actual = now.strftime("%Y-%m-%d %H:%M:%S")

nombre_archivo = now.strftime("clima-%d-%m-%y.txt")

# Guardar datos en un archivo de texto
with open(nombre_archivo, 'w') as file:
    file.write(f'Fecha y Hora de Ejecución: {fecha_hora_actual}\n')
    file.write(f'Temperatura: {temperature}\nHumedad: {humidity}\nLluvia: {rain}\nLluvia semanal: {raini}\nIntensidad: {rainw}\nLluvia mensual: {rainm}\nLluvia anual: {raina}\nRadiación: {radiation}\n Velocidad del viento: {wind} \nPunto de roció: {rocio} \nPresión: {presion}')
    
# Cerrar el navegador
driver.quit()

