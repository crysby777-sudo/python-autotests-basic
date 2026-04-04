from selenium import webdriver


driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444",
    options=webdriver.ChromeOptions()
)
driver.get("https://google.com")
driver.quit()