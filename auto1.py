from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from google.cloud import translate
from Seqmatch import similarity
from HTMLParser import HTMLParser
from sys import exit

driver = webdriver
api_key = 'AIzaSyAAa-ujxtR-A0dQc2uAQ9iwL8tEn0n00Hc'
signIn = 'sign-in-btn'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
startpractice = 'Strengthen skills'
untimed = 'untimed-button'
query = []
translate_client = translate.Client(api_key)
h = HTMLParser()
targLang = ''
rerun = 'yes'


def isitRight():
    goOn = raw_input("Does this look right? (y/n) ")
    if goOn == 'n':
        print "Please correct it. Type 'ok' when done."
        okay = raw_input("> ")


def welcome():
    print "Welcome to the AutoDuolingo program!"
    sleep(3)
    print "Lets get started, shall we?"
    sleep(3)
    print "Launching page..."
    global driver
    driver = driver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://www.duolingo.com")


def setup():
    username = raw_input("Please type your username: ")
    password = raw_input("And your password: ")
    clickLogin = driver.find_element_by_id(signIn)
    clickLogin.click()
    print "Logging in..."
    uField = driver.find_element_by_id(gotoUsername)
    uField.send_keys(username)
    pField = driver.find_element_by_id(gotoPassword)
    pField.send_keys(password)
    uField.send_keys(Keys.ENTER)


def detect_my_language():
    print "Autodetecting language..."
    sleep(8)
    detLang = driver.find_element_by_tag_name('h1')
    myLanguage = detLang.text
    languageFilter = ['Italian', 'French', 'German', 'Spanish']
    for lang in languageFilter:
        if lang in myLanguage:
            tgl = lang
    print "The program detected you are learning %s. Is this correct?" % tgl
    langConfirm = raw_input("Type 'yes' or 'no': > ")
    if langConfirm == 'yes':
        print "Great!"
        tgl = tgl.lower()
    elif langConfirm == 'no':
        print "What language are you learning?"
        tgl = raw_input("> ")
        tgl = tgl.lower()
    set_target(tgl)


def set_target(tgl):
    global targLang
    if tgl == "italian":
        targLang = 'it'
    elif tgl == "french":
        targLang = 'fr'
    elif tgl == 'german':
        targLang = 'de'
    elif tgl == "spanish":
        targLang = 'es'


def start_practice():
    skillprac = driver.find_element_by_link_text(startpractice)
    skillprac.click()
    print "Strengthening skills without timer..."
    withoutTimer = driver.find_element_by_id(untimed)
    withoutTimer.click()


def TranslateEngine():
    while True:
        print
        print "What type of page am I on? Type 'end' when you've reached the end."
        print "a: Type the translation"
        print "b: Mark correct translations"
        print "c: Speech to text translation"
        print "d: Quit the program"
        page = raw_input("> ")
        if page == 'a':
            type_The_trans()
        elif page == 'b':
            mark_Cor_trans()
        elif page == 'c':
            type_what_heard()
        elif page == 'end':
            finished_Lesson()
            break
        else:
            driver.quit()
            exit()


def type_The_trans():
    sText = driver.find_elements_by_css_selector('.non-space.token')
    for q in sText:
        query.append(q.text.encode('utf-8'))
    tText = ' '.join(query)
    setLang = translate_client.detect_language(
        tText)['language'].encode('utf-8')
    sleep(3)

    if setLang == 'en':
        engToFor = translate_client.translate(tText, target_language=targLang)[
            'translatedText']
        engToFor = h.unescape(engToFor)
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(engToFor)
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
    elif setLang == 'fr':
        frToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        frToEng = h.unescape(frToEng)
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(frToEng)
        isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'de':
        gerToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        gerToEng = h.unescape(gerToEng)
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(gerToEng)
        isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'es':
        spanToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        spanToEng = h.unescape(spanToEng)
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(spanToEng)
        isitRight()
        loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def mark_Cor_trans():
    initsentence = driver.find_element_by_xpath("(//bdi)[1]")
    text = initsentence.text
    translation = translate_client.translate(
        text, target_language=targLang)['translatedText']
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
    reset_wait_n_go()
    reset_wait_n_go()


def type_what_heard():
    print "Please type your answer here! Type replay to replay."
    answer = raw_input("> ")
    while (answer == 'replay'):
        replay = driver.find_element_by_class_name('speaker-big')
        replay.click()
        answer = raw_input("> ")
    loadResponse = driver.find_element_by_id('word-input')
    loadResponse.send_keys(answer)
    loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def reset_wait_n_go():
    del query[:]
    sleep(3)
    nextplease = driver.find_element_by_id('next_button')
    nextplease.click()


def finished_Lesson():
    print "We made it! Yay!"
    cont = driver.find_element_by_css_selector(".continue.btn.btn-lg.btn-green.right")
    cont.click()


# Commands listed here.
welcome()
setup()
while (rerun == 'yes'):
    detect_my_language()
    start_practice()
    TranslateEngine()
    rerun = raw_input("Run again? Type yes or no: ")
print "Closing down the window..."
sleep(3)
driver.quit()
