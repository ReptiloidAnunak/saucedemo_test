from time import sleep
from faker import Faker
from selenium.webdriver.common.by import By

def place_order(driver):
    btn_add_to_card = driver.find_element(By.XPATH, '//*[@id="add-to-cart"]')
    btn_add_to_card.click()
    sleep(2)
    cart_container_btn = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_container_btn.click()
    sleep(2)
    checout_btn = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checout_btn.click()
    sleep(2)

    first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    zip_postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')


    fake = Faker()

    first_name_field.click()
    first_name_field.send_keys(fake.first_name())
    sleep(2)

    last_name_field.click()
    last_name_field.send_keys(fake.last_name())
    sleep(2)

    zip_postal_code.click()
    zip_postal_code.send_keys(fake.postcode())
    sleep(2)

    continue_btn = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_btn.click()
    sleep(2)

    finish_btn = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_btn.click()
    sleep(2)

    back_home_btn = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')

    ready_msg_element = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/div')
    if 'order has been dispatched' in ready_msg_element.text:
        print(' ✅ Test passed')

    back_home_btn.click()
    sleep(2)
