from time import sleep

def scroll_from_current_position(driver, value: int):
    scroll_position = driver.execute_script("return window.scrollY;")
    driver.execute_script(f"window.scrollTo(0, {scroll_position + value});")


def scroll_to_position(driver, value: int):
    driver.execute_script(f"window.scrollTo(0, {value});")


def scroll_page_to_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(1)