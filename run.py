from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from python3_anticaptcha import NoCaptchaTaskProxyless




###################################
# I test it with Chromedriver
###################################
chrome_options = Options()

# chrome_options.add_argument("--headless")

# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options = chrome_options)


# driver = webdriver.Firefox()

driver.get("https://www.google.com/recaptcha/api2/demo")

driver.implicitly_wait(3)

# Anticaptcha key.
ANTICAPTCHA_KEY = ""
# G-ReCaptcha. Website google key.
SITE_KEY = ''
# Page url.
PAGE_URL = 'testurl'


# get service response
user_answer = NoCaptchaTaskProxyless.NoCaptchaTaskProxyless(anticaptcha_key=ANTICAPTCHA_KEY) \
    .captcha_handler(websiteURL=PAGE_URL,
                     websiteKey=SITE_KEY)
print(user_answer)

# make element visible
driver.execute_script("document.getElementById('g-recaptcha-response').style.removeProperty('display');")

# get answer from JSON service response
g_recaptcha_response = user_answer['solution']['gRecaptchaResponse']

# send g-captcha answer to form
driver.find_element_by_id('g-recaptcha-response').send_keys(g_recaptcha_response)
# submit form
driver.find_element_by_id('recaptcha-demo-submit').submit()
