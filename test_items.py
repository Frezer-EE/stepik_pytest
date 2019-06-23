from selenium import webdriver
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_existing_add_to_basket_button(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    # time.sleep(30)