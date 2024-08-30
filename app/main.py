import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chromeのオプションを設定
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# ChromeDriverのパスを指定
driver = webdriver.Chrome(options=options)

print("Starting the browser")

# Googleを開く
driver.get("https://www.google.com")

print("Browser started")

# スクリーンショットを保存するディレクトリが存在しない場合は作成
os.makedirs("./dist/", exist_ok=True)

# スクリーンショットを保存
driver.save_screenshot("./dist/screenshot.png")

print("Screenshot saved successfully")

# ブラウザを終了
driver.quit()
