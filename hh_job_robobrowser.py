from robobrowser import RoboBrowser
import configparser

namefile_cfg='config.ini'

config = configparser.ConfigParser()
config.read(namefile_cfg)

username = config['settings']['username']
parol = config['settings']['password']


user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101"
browser = RoboBrowser(user_agent=user_agent, parser='html.parser')
browser.open('https://kazan.hh.ru/account/login?backurl=%2F')
#print(browser.parsed())

# Get the signup form
signup_form = browser.get_form() # data-qa="account-login-form"

#print(signup_form)         # <RoboForm user[name]=, user[email]=, ...

# Inspect its values
# signup_form['authenticity_token'].value     # 6d03597 ...

# Fill it out
signup_form['username'].value = username
signup_form['password'].value = parol

# Serialize it to JSON
signup_form.serialize()         # {'data': {'authenticity_token': '6d03597...',
                                #  'context': '',
                                #  'user[email]': '',
                                #  'user[name]': 'python-robot',
                                #  'user[user_password]': ''}}

# And submit
browser.submit_form(signup_form)

# get source code
src = str(browser.parsed())

#print(src)

browser.open('https://kazan.hh.ru/applicant/resumes')
#print(browser.parsed())

# get buttons refresh resume
but = browser.select('.bloko-icon-link')
print(but)
print(len(but))
