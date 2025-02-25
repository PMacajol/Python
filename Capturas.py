import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit
import os
from tqdm import tqdm

# Función para tomar una captura de pantalla de un sitio web específico
def take_screenshot(url, file_name):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.save_screenshot(file_name)
    driver.quit()

# Función para enviar un mensaje de WhatsApp con la captura de pantalla usando pywhatkit
def send_whatsapp_message(group_id, message, file_path):
    pywhatkit.sendwhats_image(group_id, file_path, message, 15, True, 2)

# Función principal para tomar capturas de pantalla y enviar mensajes de WhatsApp cada hora
def main():
    url = 'http://10.2.207.200/monitoreobiweb/frmMonitoreo/frmBanca.aspx' 
    
    # ID del grupo de WhatsApp
    group_id = 'your_group_id'  # Asegúrate de usar el formato correcto para el ID del grupo
    
    # Ruta a la carpeta de Imágenes del usuario
    images_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = os.path.join(images_folder, f'screenshot_{current_time}.png')
        take_screenshot(url, file_name)
        message = f'Esta es una captura de pantalla tomada a las {current_time}.'
        send_whatsapp_message(group_id, message, file_name)
        
        # Barra de progreso para la espera de una hora
        for _ in tqdm(range(3600), desc="Esperando para el próximo mensaje"):
            time.sleep(1)

if __name__ == '__main__':
    main()
