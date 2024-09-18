from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.chrome.options import Options as ChromeOp
from selenium.webdriver.firefox.options import Options as FoxOp


def use_local_firefox_browser(geckodriver_path):
    print('\nLocal browser Firefox')
    firefox_options = Options()
    # firefox_options.add_argument('--proxy-server=1.2.3.4:8080')

    firefox_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0")
    # firefox_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
    # firefox_options.add_argument("--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0")

    # firefox_options.add_argument('--headless')

    service = Service(geckodriver_path)


    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.set_window_size(1800, 1200)
    return driver

# geckodriver_path = '/snap/bin/geckodriver'
#

def get_selenium_chrome_browser():
    print('\nSelenium Chrome browser')
    chrome_options = ChromeOp()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_selenium_firefox_browser():
    print('\nSelenium Firefox browser')
    firefox_options = FoxOp()
    # firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    return driver
