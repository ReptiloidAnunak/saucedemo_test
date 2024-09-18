from time import sleep

from app.driver.place_order import place_order
from app.driver.driver_functions import login_user, select_random_product
from errors_logs.errors_logger import save_error_log
from settings import WEBSITE
from app.driver.set_webdriver import get_selenium_chrome_browser


def run_test_main():
    driver = get_selenium_chrome_browser()
    driver.get(WEBSITE)

    login_user(driver,
               login='standard_user',
               password='secret_sauce')
    sleep(4)
    select_random_product(driver)
    place_order(driver)
    sleep(5)


if __name__ == '__main__':
    try:
        run_test_main()
    except Exception as e:
        print(e)
        print("❌❌ ERROR! ❌❌ ")
        save_error_log(str(e))

