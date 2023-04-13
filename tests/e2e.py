import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def e2e_test_service(app_url):
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get(app_url)

    # try:
    score_element = driver.find_element(By.ID, "score")
    score = score_element.text
    if 1 <= int(score) <= 1000:
        return True
    else:
        return False
    # finally:
    driver.quit()


def main_function():
    app_url = "http://127.0.0.1:5000/"
    if e2e_test_service(app_url):
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)

main_function()