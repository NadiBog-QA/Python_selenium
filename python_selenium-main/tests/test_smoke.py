from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_smoke():
    service = Service("D:\\TestProject\\SeleniumTests\\chromedriver.exe")
    driver= webdriver.Chrome(service=service)
    driver.get("https://testqastudio.me/")

    assert True, ""
    