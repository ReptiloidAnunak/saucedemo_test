from time import sleep
import random
from selenium.webdriver.common.by import By

from app.place_order import place_order
from app.driver.driver_functions import login_user, select_random_product
from settings import WEBSITE
from app.driver.set_webdriver import get_selenium_chrome_browser


def run_test_main():

    # while True:
    driver = get_selenium_chrome_browser()
    driver.get(WEBSITE)

    login_user(driver,
               login='standard_user',
               password='secret_sauce')
    sleep(4)
    select_random_product(driver)
    place_order(driver)

    sleep(1000)


if __name__ == '__main__':
    run_test_main()

