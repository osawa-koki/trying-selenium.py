from selenium import webdriver

print("Starting the browser")
driver = webdriver.Chrome()

print("Browser started")
driver.get("https://www.google.com")

driver.save_screenshot("./dist/screenshot.png")
