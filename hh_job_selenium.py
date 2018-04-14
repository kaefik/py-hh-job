import configparser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


namefile_cfg='config.ini'

config = configparser.ConfigParser()
config.read(namefile_cfg)

username = config['settings']['username']
parol = config['settings']['password']


user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101"

# настройка  Chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')
# set the window size
options.add_argument('window-size=1200x600')

# Open up a Firefox browser
#driver = webdriver.Firefox()
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://kazan.hh.ru/account/login?backurl=%2F')


elem_username = driver.find_elements_by_css_selector('input[name="username"]')
print(elem_username)
elem_username[0].send_keys(username)

elem_passwd = driver.find_elements_by_css_selector('input[name="password"]')
elem_passwd[0].send_keys(parol)

elem_submit = driver.find_elements_by_css_selector('input[type="submit"]')
elem_submit[0].click()

driver.get('https://kazan.hh.ru/applicant/resumes')

try:
    # find buttons refresh resume
    elem_but_refresh = driver.find_elements_by_css_selector('.bloko-icon-link')
    for el in elem_but_refresh:
        el.click()    
except WebDriverException:
    print("Резюме обновить нельзя. попробуйте позже.")
else:
    print("Резюме обновлено!")

driver.close()