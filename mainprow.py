from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def run_script():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://skillbox.ru")
    time.sleep(5)
    driver.quit()



if __name__ == "__main__":
    run_script()