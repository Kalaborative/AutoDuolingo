from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(15)
signIn = 'sign-in-btn'
gotoUsername = 'top_login'
gotoPassword = 'top_password'
startpractice = "Strengthen skills"
untimed = '_1pp2C'

driver.get('https://www.duolingo.com/')

driver.find_element_by_id(signIn).click()
print( "Logging in...")

uField = driver.find_element_by_id(gotoUsername)
uField.clear()
uField.send_keys("mangoHero1")
pField = driver.find_element_by_id(gotoPassword)
pField.clear()
pField.send_keys("Comput3ch")
uField.send_keys(Keys.ENTER)

print("Waiting until on a valid select page. ")
driver.find_element_by_partial_link_text("Basics 1").click()
driver.find_element_by_xpath('//*[@data-test="skill-header-practice-button"]').click()
driver.find_element_by_class_name(untimed).click()
sleep(15)

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

def test_length_of_wordbank():
	assert len(wordbank) == 3