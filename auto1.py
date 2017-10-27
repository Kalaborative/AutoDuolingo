# import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from google.cloud import translate
from Seqmatch import similarity, apostrophe_checker
from html.parser import HTMLParser
from sys import exit
import os

# set global vars
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Avid_influence.json"
driver = webdriver
api_key = 'AIzaSyAdiQFUXy5Dgr4coKTWwWJllIM5oVRUruc'
signIn = 'sign-in-btn'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
startpractice = 'Strengthen skills'
untimed = '_1pp2C'
timed = '_3XJPq'
query = []
translate_client = translate.Client()
h = HTMLParser()
targLang = ''
rerun = 'yes'


def isitRight():
        print( "Please correct it. Type Enter when done.")
        RightText = input("> ")
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.clear()
        loadResponse.send_keys(RightText)
        return 'Corrected'


def welcome():
    print( "Welcome to the AutoDuolingo program!")
    sleep(1)
    print( "Lets get started, shall we?")
    sleep(1)
    print( "Launching page...")
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })
    chrome_options.add_argument('disable-infobars')
    driver = driver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(20)
    driver.get("https://www.duolingo.com")


def setup():
    username = input("Please type your username: ")
    password = input("And your password: ")
    clickLogin = driver.find_element_by_id(signIn)
    clickLogin.click()
    print( "Logging in...")
    uField = driver.find_element_by_id(gotoUsername)
    uField.clear()
    uField.send_keys(username)
    pField = driver.find_element_by_id(gotoPassword)
    pField.clear()
    pField.send_keys(password)
    uField.send_keys(Keys.ENTER)


def detect_my_language():
    print( "Autodetecting language...")
    sleep(1)
    detLang = driver.find_element_by_tag_name('h1')
    myLanguage = detLang.text
    languageFilter = ['Italian', 'French', 'German', 'Spanish']
    for lang in languageFilter:
        if lang in myLanguage:
            tgl = lang
    print( "The program detected you are learning %s. Is this correct?" % tgl)
    langConfirm = input("Type 'yes' or 'no': > ")
    if langConfirm == 'yes':
        print( "Great!")
        tgl = tgl.lower()
    elif langConfirm == 'no':
        print( "What language are you learning?")
        tgl = input("> ")
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
    print( "Do you want to")
    print( "(a)Practice without a timer, or")
    print( "(b)Start timed practice")
    timedOrNot = input("> ")
    if timedOrNot == 'a':
        print( "Strengthening skills without timer...")
        withoutTimer = driver.find_element_by_class_name(untimed)
        withoutTimer.click()
    elif timedOrNot == 'b':
        print( "Strengthening skills with timer...")
        withTimer = driver.find_element_by_class_name(timed)
        withTimer.click()


def TranslateEngine():
    print("Type 'end' if at the end, or 'quit' to quit.")
    print("Else, just hit enter.")
    while True:
        my_choice = input("> ")
        if my_choice == "end":
            finished_Lesson()
            break
        elif my_choice == "quit":
            driver.quit()
            exit()
        else:
            header_text = driver.find_element_by_xpath('//*[@data-test="challenge-header"]').text
            if "Write this" in header_text:
                type_The_trans()
            elif "Type what you hear" in header_text:
                type_what_heard()
            elif "correct meanings" in header_text:
                mark_Cor_trans()
            else:
                print( "What type of page am I on? Type 'end' when you've reached the end.")
                print( "d: Select missing word")
                page = input("> ")
                if page == 'd':
                    select_missing()
                else:
                    print( "Please choose a valid option")


def type_The_trans():
    query = []
    sText = driver.find_elements_by_xpath('//*[@data-test="hint-token"]')
    for q in sText:
        query.append(q.text)
    tText = ' '.join(query)
    setLang = translate_client.detect_language(tText)['language']
    sleep(1)
    if setLang == 'en':
        engToFor = translate_client.translate(tText, target_language=targLang)[
            'translatedText']
        engToFor = h.unescape(engToFor)
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(engToFor)
        goOn = input("Does this look right? (y/n) ")
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'it':
        itText = apostrophe_checker(query)
        tText = ' '.join(itText)
        itToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        itToEng = h.unescape(itToEng)
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(itToEng)
        goOn = input("Does this look right? (y/n) ")
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'fr':
        frText = apostrophe_checker(query)
        tText = ' '.join(frText)
        frToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        frToEng = h.unescape(frToEng)
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(frToEng)
        goOn = input("Does this look right? (y/n) ")
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'de':
        gerToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        gerToEng = h.unescape(gerToEng)
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(gerToEng)
        goOn = input("Does this look right? (y/n) ")
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'es':
        spanToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        spanToEng = h.unescape(spanToEng)
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(spanToEng)
        goOn = input("Does this look right? (y/n) ")
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def mark_Cor_trans():
    initsentence = driver.find_element_by_class_name('KRKEd')
    text = initsentence.text
    translation = translate_client.translate(
        text, target_language=targLang)['translatedText']
    translation = h.unescape(translation)
    choices = driver.find_elements_by_xpath(
        '//*[@data-test="challenge-judge-options"]//li')
    for choice in choices:
        query.append(choice.text)
    correctedText = similarity(translation, query)
    tickboxes = driver.find_elements_by_xpath("//*[@data-test='challenge-judge-options']//label")
    for box in tickboxes:
        if correctedText in box.text:
            box.click()
    print( "I've selected: ")
    print( "'" + correctedText + "'")
    print( "If there are more solutions, type it's box number.")
    print( "Otherwise, hit enter.")
    txtbox = input("> ")
    txtbox = [t for t in txtbox if t.isdigit()]
    for x in txtbox:
        if x == '1':
            tickbox = driver.find_element_by_xpath("//*[@data-test='challenge-judge-options']//li[1]/label/div[2]")
            tickbox.click()
        elif x == '2':
            tickbox = driver.find_element_by_xpath("//*[@data-test='challenge-judge-options']//li[2]/label/div[2]")
            tickbox.click()
        elif x == '3':
            tickbox = driver.find_element_by_xpath("//*[@data-test='challenge-judge-options']//li[3]/label/div[2]")
            tickbox.click()
    reset_wait_n_go()
    reset_wait_n_go()


def type_what_heard():
    print( "Please type your answer here! Type replay to replay.")
    answer = input("> ")
    while 'replay' in answer:
        slowOrNorm = input("(1) Normal or (2) Slow? ")
        if slowOrNorm == '1':
            replay = driver.find_element_by_class_name('_3Knei')
            replay.click()
        elif slowOrNorm == '2':
            replay = driver.find_element_by_class_name('_jK6-')
            replay.click()
        answer = input("> ")
    loadResponse = driver.find_element_by_xpath("//*[@data-test='challenge-listen-input']")
    loadResponse.send_keys(answer)
    loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def select_missing():
    wordchoices = driver.find_elements_by_xpath('//option')
    wordchoices = wordchoices[1:]
    wordbank = []
    for word in wordchoices:
        wordbank.append(word.text)
    print( "Your choices are: ")
    mult = ['A] ', 'B] ', 'C] ', 'D] ', 'E] ']
    stack = zip(mult, wordbank)
    for s in stack:
        print( s[0], s[1])
    chosen = input("Which do you choose? ").upper()
    for s in stack:
        if chosen in s[0]:
            print( "You chose " + s[1] + "!")
            goodword = s[1]
    driver.find_element_by_tag_name('select').click()
    for xpaths in wordchoices:
        if xpaths.text == goodword:
            xpaths.click()
    reset_wait_n_go()
    reset_wait_n_go()


def reset_wait_n_go():
    del query[:]
    sleep(1)
    nextplease = driver.find_element_by_xpath("//*[@data-test='player-next']")
    nextplease.click()


def finished_Lesson():
    print( "We made it! Yay!")
    print( "Loading home page...")
    try:
        while True:
            cont = driver.find_element_by_xpath("//*[@data-test='player-next']")
            cont.click()
    except:
        pass


# Commands listed here.
welcome()
setup()
while (rerun == 'yes'):
    try:
        detect_my_language()
        start_practice()
        TranslateEngine()
        rerun = input("Run again? Type yes or no: ")
    except Exception as e:
        print(e)
        break
print( "Closing down the window...")
sleep(1)
driver.quit()
