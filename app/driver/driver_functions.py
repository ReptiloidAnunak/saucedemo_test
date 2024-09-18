from time import sleep
import random
from faker import Faker
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from app.driver.driver_tools import scroll_to_element


def login_user(driver,
               login,
               password):
    username_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    pwd_unput = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_btn = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username_input.click()
    sleep(1)
    username_input.send_keys(login)
    sleep(1)

    pwd_unput.click()
    sleep(1)
    pwd_unput.send_keys(password)
    sleep(1)
    login_btn.click()


def select_random_product(driver):
    products_lst = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div')
    products_cards = products_lst.find_elements(By.CLASS_NAME, 'inventory_item')


    random_product = random.choice(products_cards)
    #
    try:
        scroll_to_element(driver, random_product)
        title_link = random_product.find_element(By.CLASS_NAME, 'inventory_item_name ')
        sleep(2)
        title_link.click()
    except NoSuchElementException:
        print("NoSuchElementException")
    except Exception as e:
        print(f"ERROR: {e}")





