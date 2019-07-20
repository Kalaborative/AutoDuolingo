#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print("Here we go!")
print('Enter email: ')
email = input()
print('Enter pass: ')
passw = input()


global driver
driver = webdriver
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_argument('disable-infobars')
driver = driver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
#driver.maximize_window()
driver.get("https://www.duolingo.com/log-in")
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[1]/div/input').send_keys(email)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[2]/div/input').send_keys(passw)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click()
sleep(5)

def x(xpath):
    return driver.find_element_by_xpath(xpath)

def skip():
    while True:
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[1]/button').click()
        x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
        sleep(1)

def url():
    driver.get('https://www.duolingo.com/skill/ar/Alphabet1/practice')
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button[2]').click()

def solve():
    challenge = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/h1/span').text    
    print(challenge)
    try:
        if challenge:
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[1]/button').click()
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
            sleep(0.5)
            challenge = ''
        else:
            print('Challenge is empty, getting text')
    except:
        print('Entered exception, trying again')
        pass
        url()
    solve()

url()
solve()
