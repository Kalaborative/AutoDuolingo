import os
from html.parser import HTMLParser
from sys import exit
from time import sleep

# import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Seqmatch import apostrophe_checker, similarity

# set global vars
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloudcreds.json"
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Avid_influence.json"
driver = webdriver
api_key = 'AIzaSyAdiQFUXy5Dgr4coKTWwWJllIM5oVRUruc'
signIn = 'sign-in-btn'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
wrongChallenges = []
startpractice = 'Strengthen skills'
untimed = '_1pp2C'
timed = '_3XJPq'
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
    print( "Here we go!")
    global driver
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
    driver.get("https://www.duolingo.com/log-in")
    emailField = driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[1]/div/input')
    emailField.send_keys('nneauu@gmail.com')
    pF = driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[2]/div/input')
    pF.send_keys('sewd34Rf')
    driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click()

def skill_or_practice():
	driver.get('https://www.duolingo.com/practice')
	start_practice()

def practice_topic():
    skills = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button[2]')
    
    
    list_of_skills = []
    for skill in skills:
    	list_of_skills.append(skill.text)

    desired_skill = input("Which skill would you like to learn? ")

    matching_skills = [skill for skill in list_of_skills if desired_skill in skill]

    if len(matching_skills) > 1:
    	print("Matching choices are: ")
    	for skill in matching_skills:
    		print(skill)
    	print("Which one do you choose? ")
    	chosen_skill = input()
    elif len(matching_skills) == 0:
    	print("Could not find a matching skill.")
    	exit()
    else:
    	chosen_skill = matching_skills[0]

    driver.find_element_by_partial_link_text(chosen_skill).click()
    sleep(1)
    print("Would you like to test out this skill? Y or N")
    test_out = input("> ")
    if test_out.lower() == "y":
        driver.find_element_by_class_name('_1Le6e').click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
        sleep(1)
        driver.find_element_by_class_name('_3XJPq').click()
    else:
        driver.find_element_by_class_name('_3ntRm').click()

def start_practice():
    withoutTimer = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button[1]')
    withoutTimer.click()


def TranslateEngine():
        header_text = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/h1/span').text
        print('The value of current challenge is: ', header_text)

        if "Write this" in header_text:
            type_The_trans()
        elif "Type what you hear" in header_text:
            type_what_heard()
        elif "Mark the correct meaning" in header_text:
            mark_Cor_trans()
        elif "Select the missing word" in header_text:
            select_missing()
        elif 'Select the word for' in header_text:
                word_for(header_text)
                mark_Cor_trans()
        elif 'What sound does this make?' in header_text:
                word_for(header_text)
        #except:
        #    finished_Lesson()
        #    break

def word_for(a):
        challenge = '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/span'
        cL = driver.find_element_by_xpath(challenge).text
        
        b1 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/label/div[2]')
        b2 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/label/div[2]')
        b3 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/label/div[2]')

        a1 = b1.text
        a2 = b2.text
        a3 = b3.text

        print('challenge is ', cL)
        if 'وي' in cL:
                ca = 'wii'
        elif 'زود' in cL:
                ca = 'zuud'
        elif 'زو' in cL:
                ca = 'zuu'
        elif 'وا' in cL:
                ca = 'waa'
        elif 'دَ' in cL:
                ca = 'da'
        elif 'دا' in cL:
                ca = 'daa'
        elif 'زَ' in cL:
                ca = 'za'
        elif 'ي' in cL:
                ca = 'ii'
        else:
                ca = '[blank ca]'
                print('could not find correct answer for ', cL, 'options are ', a1, a2, a3, '[', ca, ']', sep=' ')
        print('ca is: ', ca)

        sleep(1)
        if cL in a1:
                b1.click()
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/label').click()        
        elif cL in a2:
                b2.click()
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/label').click()        
        elif cL in a3:
                b3.click()
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/label').click()        
        else:
                print('Unhandled exception,', cL, a1, a2, a3)

        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button..\.').click()

        sleep(3)

def mark_Cor_trans():
    query = []
    initsentence = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[1]')
    text = initsentence.text
    print('#bdb Text to be evaluated is ', text)
    translation = translate_client.translate(text, target_language='de')['translatedText']
    translation = h.unescape(translation)

    if text == 'The beatles are eating the bananas.':
        translation = 'Die Käfer essen die Bananen'
    elif text == 'The bird is eating the flies.':
        translation = 'Der Vogel frisst die Fliegen'
    elif text == 'The cows have flies.':
        translation = 'Die Kühe haben Fliegen'
            
    print('#bdb Translation is: ', translation)
    choices = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/ul/li')
    for choice in choices:
        print('Trying choice: ', choice.text)
        print('choice is :', choice)
        query.append(choice.text)
    correctedText = similarity(translation, query)
    tickboxes = driver.find_elements_by_xpath("//*[@data-test='challenge-judge-options']//label")
    for box in tickboxes:
        if correctedText in box.text:
            print('#bdb box.text = ', box.text, 'also, ', box)
            box.click()
    print( "I've selected: ")
    print( correctedText )
    print( "If there are more solutions, type it's box number.")
    print( "Otherwise, hit enter.")
    txtbox = input("> ")
    txtbox = [t for t in txtbox if t.isdigit()]
    for x in txtbox:
        tickbox = driver.find_element_by_xpath("//*[@data-test='challenge-judge-options']//li[{}]/label/div[2]".format(x))
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
    loadResponse = driver.find_element_by_xpath("//*[@data-test='challenge-listentap-input']")
    loadResponse.send_keys(answer)
    loadResponse.send_keys(Keys.ENTER)
    reset_wait_n_go()


def select_missing():
    all_words = driver.find_elements_by_xpath("//*[@data-test='challenge-select']")
    wordbank = []
    for word in all_words:
        wordbank.append(word.text)
    words = [w[2:] for w in wordbank]
    numbers = [w[0] + "] " for w in wordbank] 
    print( "Your choices are: ")
    stack = list(zip(numbers, words))
    for s in stack:
        print( s[0], s[1])
    number_choice = input("Which do you choose? ")
    for word in all_words:
        if number_choice in word.text:
            word.click()
    reset_wait_n_go()
    reset_wait_n_go()


def reset_wait_n_go():
    next_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@data-test='player-next']"))
        )
    next_button = driver.find_element_by_xpath("//*[@data-test='player-next']")
    next_button.click()


def finished_Lesson():
    print( "We made it! Yay!")
    print( "Loading home page...")
    sleep(3)
    try:
        while True:
            cont = driver.find_element_by_xpath("//*[@data-test='player-next']")
            cont.click()
            sleep(1)
    except:
        driver.get("https://duolingo.com")


# Commands listed here.
if __name__ == "__main__":
	welcome();sleep(5)
	while True:
	    try:
	        skill_or_practice()
	        TranslateEngine()
	    except Exception as e:
	        raise e
	        break
	print( "Closing down the window...")
	sleep(1)
	driver.quit()
