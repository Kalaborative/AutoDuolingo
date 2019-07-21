#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print("Here we go!")
#print('Enter email: ')
email = ''
#print('Enter pass: ')
passw = ''


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
driver.maximize_window()
skipped = 0
d = {'وا':'waa','رَ':'ra','دَ':'da','وي':'wii','دا':'daa','زود':'zuud','زار':'zaar','داد':'daad','زَ':'za','وَ':'wa','زو':'zuu','راي':'raay','يَ':'ya','زي':'zii','زو':'zuu','دي':'dii','زا':'zaa','رو':'ruu','رود':'ruud','رَ':'ra','را':'raa','دور':'duur','ي':'ii','دو':'duu','دود':'duud','و':'uu','راو':'raaw','ا':'aa','وو':'wuu','ري':'rii'}

#Begin 
driver.get("https://www.duolingo.com/log-in")
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[1]/div/input').send_keys(email)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[2]/div/input').send_keys(passw)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click()
sleep(5)

def x(xpath):
    return driver.find_element_by_xpath(xpath)

def skip():
    print('Skipping...')
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[1]/button').click()
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
    sleep(0.5)

def url():
    driver.get('https://www.duolingo.com/skill/ar/Alphabet1/practice')
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button[2]').click()

def solve():
    challenge = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/h1/span').text    
    print('\nNew challenge: ',challenge)
    try:
        if 'Match the pairs' in challenge:
            print('TYPE: Math the pairs')
            skip()
        elif 'What sound does this make?' in challenge:
            print('TYPE: What sound does this make?')
            challengeLetter = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/span').text
            print('Challenge is: ', challengeLetter)
            c = d.get(challengeLetter)
            print('Answer should be: ', c)

            a1 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/label/div[2]').text
            print('Answer1: ', a1)
            a2 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/label/div[2]').text
            print('Answer2: ', a2)
            a3 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/label/div[2]').text
            print('Answer3: ', a3)
            
            if c == a1:
                print('>>1')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/label/div[2]').click()
            elif c == a2:
                print('>>2')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/label/div[2]').click()
            elif c == a3:
                print('>>3')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/label/div[2]').click()
            else:
                print('Challenge not found, letter: ', challengeLetter, ', Options', b1.text, b2.text, b3.text)
                skip()
            # Assuming correct answer is selected, check and move on
            # Check
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button').click()
            # Continue
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
            sleep(0.5)               
        else:
            print('ENTERED ELSE, SKIPPING for'       )
            skip()
    except:
        print('\nNo more challenges detected, refreshing', challenge)
        return
    solve()

while True:
    url()
    solve()
