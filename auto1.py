from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from google.cloud import translate
from Seqmatch import similarity
from HTMLParser import HTMLParser


def isitRight():
    goOn = raw_input("Does this look right? (y/n) ")
    if goOn == 'n':
        print "Please correct it. Type 'ok' when done."
        okay = raw_input("> ")


print "Launching page..."
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.duolingo.com")

api_key = 'AIzaSyAAa-ujxtR-A0dQc2uAQ9iwL8tEn0n00Hc'
signIn = 'sign-in-btn'
username = 'mangoHero1'
password = 'Comput3ch'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
startpractice = 'Strengthen skills'
untimed = 'untimed-button'

clickLogin = driver.find_element_by_id(signIn)
clickLogin.click()
print "Logging in..."
uField = driver.find_element_by_id(gotoUsername)
uField.send_keys(username)

pField = driver.find_element_by_id(gotoPassword)
pField.send_keys(password)
uField.send_keys(Keys.ENTER)

skillprac = driver.find_element_by_link_text(startpractice)
skillprac.click()
print "Strengthening skills without timer..."
withoutTimer = driver.find_element_by_id(untimed)
withoutTimer.click()

query = []
translate_client = translate.Client(api_key)
h = HTMLParser()

while True:
    print "What type of page am I on? Type 'end' when you've reached the end."
    print "a: Type the translation"
    print "b: Mark correct translations"
    print "c: Speech to text translation"
    print "d: Quit the program"
    page = raw_input("> ")
    if page == 'a':
        sText = driver.find_elements_by_css_selector('.non-space.token')
        for q in sText:
            query.append(q.text.encode('utf-8'))
        tText = ' '.join(query)
        setLang = translate_client.detect_language(
            tText)['language'].encode('utf-8')
        query = []
        sleep(3)

        if setLang == 'en':
            engToIt = translate_client.translate(tText, target_language='it')[
                'translatedText']
            engToIt = h.unescape(engToIt)
            loadResponse = driver.find_element_by_id('text-input')
            loadResponse.send_keys(engToIt)
            isitRight()
            loadResponse.send_keys(Keys.ENTER)
        elif setLang == 'it':
            itToEng = translate_client.translate(tText, target_language='en')[
                'translatedText']
            itToEng = h.unescape(itToEng)
            loadResponse = driver.find_element_by_id('text-input')
            loadResponse.send_keys(itToEng)
            isitRight()
            loadResponse.send_keys(Keys.ENTER)
        sleep(3)
        nextplease = driver.find_element_by_id('next_button')
        nextplease.click()
    elif page == 'b':
        initsentence = driver.find_element_by_xpath("(//bdi)[1]")
        text = initsentence.text
        translation = translate_client.translate(
            text, target_language='it')['translatedText']
        translation = h.unescape(translation)
        choices = driver.find_elements_by_xpath(
            '//ul[@class="list-judge-options hover-effect"]//bdi')
        for choice in choices:
            query.append(choice.text)
        correctedText = similarity(translation, query)
        print "Which text box has this answer?"
        print "'" + correctedText + "'"
        txtbox = raw_input("> ")
        if txtbox == '1':
        	tickbox = driver.find_element_by_xpath('//*[@id="sentence-0"]')
        	tickbox.click()
        elif txtbox == '2':
        	tickbox = driver.find_element_by_xpath('//*[@id="sentence-1"]')
        	tickbox.click()
        elif txtbox == '3':
        	tickbox = driver.find_element_by_xpath('//*[@id="sentence-2"]')
        	tickbox.click()
        sleep(4)
        query = []
        nextplease = driver.find_element_by_id('next_button')
        nextplease.click()
        sleep(1)
        nextplease.click()
    elif page == 'c':
    	print "Please type your answer here! Type replay to replay."
    	answer = raw_input("> ")
    	while (answer == 'replay'):
    		replay = driver.find_element_by_class_name('speaker-big')
    		replay.click()
    		answer = raw_input("> ")
    	loadResponse = driver.find_element_by_id('word-input')
        loadResponse.send_keys(answer)
        loadResponse.send_keys(Keys.ENTER)
        sleep(3)
        nextplease = driver.find_element_by_id('next_button')
        nextplease.click()
    elif page == 'end':
    	print "We made it! Yay!"
    	cont = driver.find_element_by_css_selector(".continue.btn.btn-lg.btn-green.right")
    	cont.click()
    	print "Closing down the window..."
    	sleep(3)
    	driver.quit()
    	break
    else:
        driver.quit()
        break
