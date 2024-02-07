from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar opciones para el navegador Chrome en modo headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
chrome_options.add_argument('--no-sandbox')  # Bypass del modo de sandboxing
chrome_options.add_argument('--disable-dev-shm-usage')  # Deshabilitar el uso compartido de memoria temporal

# Inicializar el navegador Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Lista para almacenar los nombres de los iconos
icon_names = []

# Abrir la página
driver.get('https://fontawesome.com/search?p=1')

# Esperar hasta que los elementos de los iconos estén visibles en el DOM
wait = WebDriverWait(driver, 10)
icon_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'article.wrap-icon.with-top-tag button span.icon-name')))

# Extraer los nombres de los iconos y agregarlos a la lista
for icon_element in icon_elements:
    icon_name = icon_element.text.strip()
    if icon_name:
        icon_names.append(icon_name)

# Imprimir los nombres de los iconos
for name in icon_names:
    print(name)

# Cerrar el navegador
driver.quit()