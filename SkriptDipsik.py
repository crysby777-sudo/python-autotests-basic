from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_script():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        # Ожидание готовности браузера
        time.sleep(2)
        driver.maximize_window()
        driver.get("https://github.com")
        # ... остальные действия
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    run_script()