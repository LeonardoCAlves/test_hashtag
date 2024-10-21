from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
import csv
from time import sleep
import os

# Configurar as opções do Chrome
chrome_options = Options()

# Usar o WebDriver Manager para instalar o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navegar até a página
driver.get('https://dlp.hashtagtreinamentos.com/python/intensivao/login?ps=incompany')

# Esperar o campo de e-mail aparecer
wait = WebDriverWait(driver, 10)

try:
    # Verificar se há um alerta presente e fechá-lo
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alerta encontrado: {alert_text}")
    alert.accept()  # Aceita (fecha) o alerta

except NoAlertPresentException as e:
    print(e)

# Continuar com o código de login
email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email_input.send_keys('leon4rdoalvess@gmail.com')

# Esperar o campo de senha aparecer
senha_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))

# senha = os.getenv("emailPassword")
senha_input.send_keys(os.getenv("EMAIL_PASS"))

# Submeter o formulário de login
senha_input.submit()

# Esperar a próxima página carregar, por exemplo
sleep(2)

# codigo marca tipo categoria preco_unitario custo obs

with open('base/produtos.csv', newline='', encoding='utf-8') as file:
    dados = csv.DictReader(file)
    
    # Iterar sobre cada linha do CSV e preencher os campos do formulário
    for linha in dados:
        # Preencher os campos de produto
        codigo_input = wait.until(EC.presence_of_element_located((By.ID, 'codigo')))
        codigo_input.clear()  # Limpar antes de inserir
        codigo_input.send_keys(linha['codigo'])

        marca_input = driver.find_element(By.ID, 'marca')
        marca_input.clear()
        marca_input.send_keys(linha['marca'])

        tipo_input = driver.find_element(By.ID, 'tipo')
        tipo_input.clear()
        tipo_input.send_keys(linha['tipo'])

        categoria_input = driver.find_element(By.ID, 'categoria')
        categoria_input.clear()
        categoria_input.send_keys(linha['categoria'])

        preco_input = driver.find_element(By.ID, 'preco_unitario')
        preco_input.clear()
        preco_input.send_keys(linha['preco_unitario'])

        custo_input = driver.find_element(By.ID, 'custo')
        custo_input.clear()
        custo_input.send_keys(linha['custo'])

        obs_input = driver.find_element(By.ID, 'obs')
        obs_input.clear()
        obs_input.send_keys(linha['obs'])

        sleep(1)

        # Submeter o formulário
        submit_button = driver.find_element(By.ID, 'pgtpy-botao') 
        submit_button.click()

        # Esperar um pouco entre cada envio
        sleep(1)

# Fecha o navegador
driver.quit()

