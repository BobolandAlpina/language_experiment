from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_cart_btn(browser):
    browser.get(link)
    time.sleep(1)
    submit_btn = browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")
    submit_btn.click()
    #стоит добавить более чёткий путь до элемента