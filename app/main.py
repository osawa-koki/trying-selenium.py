from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--lang=en-US")

driver = webdriver.Chrome(options=options)

count = 0


def screenshot(driver):
    global count
    count += 1
    driver.implicitly_wait(2)
    driver.save_screenshot(f"./dist/{count}.png")


try:
    driver.get("https://www.google.com")
    screenshot(driver)

    q = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) # noqa
    q.send_keys("Python")
    screenshot(driver)

    q.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains("Python"))
    screenshot(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    screenshot(driver)

    next_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "2"))
    )
    next_page.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Python"))
    screenshot(driver)

    driver.get("https://www.google.com")
    screenshot(driver)

    q = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) # noqa
    q.send_keys("askew")
    screenshot(driver)
    q.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains("askew"))
    screenshot(driver)

    driver.get("https://www.google.com")
    screenshot(driver)

    q = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) # noqa
    q.send_keys("the number of horns on a unicorn")
    screenshot(driver)
    q.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.title_contains("the number of horns on a unicorn")
    )
    screenshot(driver)

finally:
    driver.quit()
