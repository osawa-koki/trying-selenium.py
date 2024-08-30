from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

count = 0


def screenshot(driver):
    global count
    count += 1
    driver.save_screenshot(f"./dist/{count}.png")


driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
screenshot(driver)

q = driver.find_element(By.NAME, "q")
q.send_keys("Japan")
screenshot(driver)

search = driver.find_element(By.NAME, "btnK")
search.click()
screenshot(driver)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
screenshot(driver)

next_page = driver.find_element(By.LINK_TEXT, "2")
next_page.click()
screenshot(driver)

images = driver.find_element(By.LINK_TEXT, "画像")
images.click()
screenshot(driver)

driver.quit()
