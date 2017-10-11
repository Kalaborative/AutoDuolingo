<<<<<<< HEAD
=======
# import necessary modules
>>>>>>> py2 to py3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from google.cloud import translate
from Seqmatch import similarity, apostrophe_checker
<<<<<<< HEAD
from HTMLParser import HTMLParser
from sys import exit

driver = webdriver
api_key = 'AIzaSyAAa-ujxtR-A0dQc2uAQ9iwL8tEn0n00Hc'
=======
from html.parser import HTMLParser
from sys import exit
import os

# set global vars
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Avid_influence.json"
driver = webdriver
api_key = 'AIzaSyAdiQFUXy5Dgr4coKTWwWJllIM5oVRUruc'
>>>>>>> py2 to py3
signIn = 'sign-in-btn'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
startpractice = 'Strengthen skills'
<<<<<<< HEAD
untimed = 'untimed-button'
timed = 'start-button'
query = []
translate_client = translate.Client(api_key)
=======
untimed = '_1pp2C'
timed = '_3XJPq'
query = []
translate_client = translate.Client()
>>>>>>> py2 to py3
h = HTMLParser()
targLang = ''
rerun = 'yes'


def isitRight():
<<<<<<< HEAD
        print "Please correct it. Type Enter when done."
        RightText = raw_input("> ")
        loadResponse = driver.find_element_by_id('text-input')
=======
        print( "Please correct it. Type Enter when done.")
        RightText = input("> ")
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
>>>>>>> py2 to py3
        loadResponse.clear()
        loadResponse.send_keys(RightText)
        return 'Corrected'


def welcome():
<<<<<<< HEAD
    print "Welcome to the AutoDuolingo program!"
    sleep(3)
    print "Lets get started, shall we?"
    sleep(3)
    print "Launching page..."
    global driver
    driver = driver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
=======
    print( "Welcome to the AutoDuolingo program!")
    sleep(3)
    print( "Lets get started, shall we?")
    sleep(3)
    print( "Launching page...")
    global driver
    driver = driver.Chrome()
    driver.implicitly_wait(20)
>>>>>>> py2 to py3
    driver.get("https://www.duolingo.com")


def setup():
<<<<<<< HEAD
    username = raw_input("Please type your username: ")
    password = raw_input("And your password: ")
    clickLogin = driver.find_element_by_id(signIn)
    clickLogin.click()
    print "Logging in..."
=======
    username = input("Please type your username: ")
    password = input("And your password: ")
    clickLogin = driver.find_element_by_id(signIn)
    clickLogin.click()
    print( "Logging in...")
>>>>>>> py2 to py3
    uField = driver.find_element_by_id(gotoUsername)
    uField.clear()
    uField.send_keys(username)
    pField = driver.find_element_by_id(gotoPassword)
    pField.clear()
    pField.send_keys(password)
    uField.send_keys(Keys.ENTER)


def detect_my_language():
<<<<<<< HEAD
    print "Autodetecting language..."
=======
    print( "Autodetecting language...")
>>>>>>> py2 to py3
    sleep(8)
    detLang = driver.find_element_by_tag_name('h1')
    myLanguage = detLang.text
    languageFilter = ['Italian', 'French', 'German', 'Spanish']
    for lang in languageFilter:
        if lang in myLanguage:
            tgl = lang
<<<<<<< HEAD
    print "The program detected you are learning %s. Is this correct?" % tgl
    langConfirm = raw_input("Type 'yes' or 'no': > ")
    if langConfirm == 'yes':
        print "Great!"
        tgl = tgl.lower()
    elif langConfirm == 'no':
        print "What language are you learning?"
        tgl = raw_input("> ")
=======
    print( "The program detected you are learning %s. Is this correct?" % tgl)
    langConfirm = input("Type 'yes' or 'no': > ")
    if langConfirm == 'yes':
        print( "Great!")
        tgl = tgl.lower()
    elif langConfirm == 'no':
        print( "What language are you learning?")
        tgl = input("> ")
>>>>>>> py2 to py3
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
<<<<<<< HEAD
    print "Do you want to"
    print "(a)Practice without a timer, or"
    print "(b)Start timed practice"
    timedOrNot = raw_input("> ")
    if timedOrNot == 'a':
        print "Strengthening skills without timer..."
        withoutTimer = driver.find_element_by_id(untimed)
        withoutTimer.click()
    elif timedOrNot == 'b':
        print "Strengthening skills with timer..."
        withTimer = driver.find_element_by_id(timed)
=======
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
>>>>>>> py2 to py3
        withTimer.click()


def TranslateEngine():
    while True:
        print
<<<<<<< HEAD
        print "What type of page am I on? Type 'end' when you've reached the end."
        print "a: Type the translation"
        print "b: Mark correct translations"
        print "c: Speech to text translation"
        print "d: Select missing word"
        print "e: Quit the program"
        page = raw_input("> ")
=======
        print( "What type of page am I on? Type 'end' when you've reached the end.")
        print( "a: Type the translation")
        print( "b: Mark correct translations")
        print( "c: Speech to text translation")
        print( "d: Select missing word")
        print( "e: Quit the program")
        page = input("> ")
>>>>>>> py2 to py3
        if page == 'a':
            sleep(1)
            type_The_trans()
        elif page == 'b':
            mark_Cor_trans()
        elif page == 'c':
            type_what_heard()
        elif page == 'd':
            select_missing()
        elif page == 'e':
            driver.quit()
            exit()
        elif page == 'end':
            finished_Lesson()
            break
        else:
<<<<<<< HEAD
            print "Please choose a valid option"


def type_The_trans():
    sText = driver.find_elements_by_css_selector('.non-space.token')
    for q in sText:
        query.append(q.text.encode('utf-8'))
    tText = ' '.join(query)
    setLang = translate_client.detect_language(
        tText)['language'].encode('utf-8')
=======
            print( "Please choose a valid option")


def type_The_trans():
    global query
    sText = driver.find_elements_by_xpath('//*[@data-test="hint-token"]')
    for q in sText:
        query.append(q.text)
    tText = ' '.join(query)
    setLang = translate_client.detect_language(tText)['language']
>>>>>>> py2 to py3
    sleep(3)

    if setLang == 'en':
        engToFor = translate_client.translate(tText, target_language=targLang)[
            'translatedText']
        engToFor = h.unescape(engToFor)
<<<<<<< HEAD
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(engToFor)
        goOn = raw_input("Does this look right? (y/n) ")
=======
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(engToFor)
        goOn = input("Does this look right? (y/n) ")
>>>>>>> py2 to py3
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'it':
        itText = apostrophe_checker(query)
        tText = ' '.join(itText)
        itToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        itToEng = h.unescape(itToEng)
<<<<<<< HEAD
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(itToEng)
        goOn = raw_input("Does this look right? (y/n) ")
=======
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(itToEng)
        goOn = input("Does this look right? (y/n) ")
>>>>>>> py2 to py3
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'fr':
        frText = apostrophe_checker(query)
        tText = ' '.join(frText)
        frToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        frToEng = h.unescape(frToEng)
<<<<<<< HEAD
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(frToEng)
        goOn = raw_input("Does this look right? (y/n) ")
=======
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(frToEng)
        goOn = input("Does this look right? (y/n) ")
>>>>>>> py2 to py3
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'de':
        gerToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        gerToEng = h.unescape(gerToEng)
<<<<<<< HEAD
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(gerToEng)
        goOn = raw_input("Does this look right? (y/n) ")
=======
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(gerToEng)
        goOn = input("Does this look right? (y/n) ")
>>>>>>> py2 to py3
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    elif setLang == 'es':
        spanToEng = translate_client.translate(tText, target_language='en')[
            'translatedText']
        spanToEng = h.unescape(spanToEng)
<<<<<<< HEAD
        loadResponse = driver.find_element_by_id('text-input')
        loadResponse.send_keys(spanToEng)
        goOn = raw_input("Does this look right? (y/n) ")
=======
        loadResponse = driver.find_element_by_xpath('//*[@data-test="challenge-translate-input"]')
        loadResponse.send_keys(spanToEng)
        goOn = input("Does this look right? (y/n) ")
>>>>>>> py2 to py3
        if goOn == 'n':
            isitRight()
        loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def mark_Cor_trans():
<<<<<<< HEAD
    initsentence = driver.find_element_by_xpath("(//bdi)[1]")
=======
    initsentence = driver.find_element_by_class_name('KRKEd')
>>>>>>> py2 to py3
    text = initsentence.text
    translation = translate_client.translate(
        text, target_language=targLang)['translatedText']
    translation = h.unescape(translation)
    choices = driver.find_elements_by_xpath(
<<<<<<< HEAD
        '//ul[@class="list-judge-options hover-effect"]//bdi')
    for choice in choices:
        query.append(choice.text)
    correctedText = similarity(translation, query)
    tickboxes = driver.find_elements_by_css_selector('.white-label.cb-container-long')
    for box in tickboxes:
        if correctedText in box.text:
            box.click()
    print "I've selected: "
    print "'" + correctedText + "'"
    print "If there are more solutions, type it's box number."
    print "Otherwise, hit enter."
    txtbox = raw_input("> ")
    txtbox = [t for t in txtbox if t.isdigit()]
    for x in txtbox:
        if x == '1':
            tickbox = driver.find_element_by_xpath('//*[@id="sentence-0"]')
            tickbox.click()
        elif x == '2':
            tickbox = driver.find_element_by_xpath('//*[@id="sentence-1"]')
            tickbox.click()
        elif x == '3':
            tickbox = driver.find_element_by_xpath('//*[@id="sentence-2"]')
=======
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
>>>>>>> py2 to py3
            tickbox.click()
    reset_wait_n_go()
    reset_wait_n_go()


def type_what_heard():
<<<<<<< HEAD
    print "Please type your answer here! Type replay to replay."
    answer = raw_input("> ")
    while 'replay' in answer:
        slowOrNorm = raw_input("(1) Normal or (2) Slow? ")
        if slowOrNorm == '1':
            replay = driver.find_element_by_class_name('speaker-big')
            replay.click()
        elif slowOrNorm == '2':
            replay = driver.find_element_by_class_name('speaker-slow')
            replay.click()
        answer = raw_input("> ")
    loadResponse = driver.find_element_by_id('word-input')
=======
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
>>>>>>> py2 to py3
    loadResponse.send_keys(answer)
    loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def select_missing():
    wordchoices = driver.find_elements_by_xpath('//option')
    wordchoices = wordchoices[1:]
    wordbank = []
    for word in wordchoices:
        wordbank.append(word.text)
<<<<<<< HEAD
    print "Your choices are: "
    mult = ['A] ', 'B] ', 'C] ', 'D] ', 'E] ']
    stack = zip(mult, wordbank)
    for s in stack:
        print s[0], s[1]
    chosen = raw_input("Which do you choose? ").upper()
    for s in stack:
        if chosen in s[0]:
            print "You chose " + s[1] + "!"
=======
    print( "Your choices are: ")
    mult = ['A] ', 'B] ', 'C] ', 'D] ', 'E] ']
    stack = zip(mult, wordbank)
    for s in stack:
        print( s[0], s[1])
    chosen = input("Which do you choose? ").upper()
    for s in stack:
        if chosen in s[0]:
            print( "You chose " + s[1] + "!")
>>>>>>> py2 to py3
            goodword = s[1]
    driver.find_element_by_tag_name('select').click()
    for xpaths in wordchoices:
        if xpaths.text == goodword:
            xpaths.click()
    reset_wait_n_go()
    reset_wait_n_go()


def reset_wait_n_go():
    del query[:]
    sleep(3)
<<<<<<< HEAD
    nextplease = driver.find_element_by_id('next_button')
=======
    nextplease = driver.find_element_by_xpath("//*[@data-test='player-next']")
>>>>>>> py2 to py3
    nextplease.click()


def finished_Lesson():
<<<<<<< HEAD
    print "We made it! Yay!"
    cont = driver.find_element_by_css_selector(".continue.btn.btn-lg.btn-green.right")
=======
    print( "We made it! Yay!")
    cont = driver.find_element_by_xpath("//*[@data-test='player-next']")
>>>>>>> py2 to py3
    cont.click()


# Commands listed here.
welcome()
setup()
while (rerun == 'yes'):
    try:
        detect_my_language()
        start_practice()
        TranslateEngine()
<<<<<<< HEAD
        rerun = raw_input("Run again? Type yes or no: ")
    except:
        print "Your login info was incorrect. Please try again!"
        clickLogin = driver.find_element_by_id(signIn)
        clickLogin.click()
        setup()
print "Closing down the window..."
=======
        rerun = input("Run again? Type yes or no: ")
    except Exception as e:
        print(e)
        print( "Your login info was incorrect. Please try again!")
        clickLogin = driver.find_element_by_id(signIn)
        clickLogin.click()
        setup()
print( "Closing down the window...")
>>>>>>> py2 to py3
sleep(3)
driver.quit()
