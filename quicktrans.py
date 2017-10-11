# Greetings! In this file, we're going to be using
# Google's client library to translate some text
# to another language. This is gonna be exciting!

from google.cloud import translate
from time import sleep
from sys import exit
<<<<<<< HEAD
api_key = 'AIzaSyCshp5LS_bmxQR6-vqGP6f5apFpw9vmVrQ'
=======
api_key = 'AIzaSyAdiQFUXy5Dgr4coKTWwWJllIM5oVRUruc'
>>>>>>> py2 to py3

langcodes = {
	"arabic": "ar",
	"czech": "cs",
	"chinese": "zh",
	"danish": "da",
	"german": "de",
	"dutch": "nl",
	"french": "fr",
	"hindi": "hi",
	"gujarati": "gu",
	"italian": "it",
	"japanese": "ja",
	"korean": "ko",
	"latin": "la",
	"portuguese": "pt",
	"russian": "ru",
	"spanish": "es",
	"swedish": "sv",
	"turkish": "tr",
	"vietnamese": "vi"
}


def resultcode(text, target, reqlang):

	# Instantiates a client
<<<<<<< HEAD
	translate_client = translate.Client(api_key)

	translation = translate_client.translate(text, target_language=target)
	print ("\n" * 100)
	print 'Your text was..'
	sleep(2)
	print text
	sleep(2)
	print
	print "Translating into %s..." % reqlang
	sleep(5)
	print 'Translation: %s ' % translation['translatedText']
=======
	translate_client = translate.Client()

	translation = translate_client.translate(text, target_language=target)
	print ("\n" * 100)
	print( 'Your text was..')
	sleep(2)
	print( text)
	sleep(2)
	print
	print( "Translating into %s..." % reqlang)
	sleep(5)
	print( 'Translation: %s ' % translation['translatedText'])
>>>>>>> py2 to py3


def rerun():
	sleep(2)
<<<<<<< HEAD
	print "Would you like to run this program again? (Y/N)"
	runagain = raw_input("> ").lower()
=======
	print( "Would you like to run this program again? (Y/N)")
	runagain = input("> ").lower()
>>>>>>> py2 to py3
	if runagain == 'y':
		mainmenu()
	else:
		exit()


def mainmenu():
	print ("\n" * 100)
<<<<<<< HEAD
	print "Welcome to my translation program!"
	print "What would you like to do?"
	print "A) Translate something to English"
	print "B) Translate English to some other language"
	mychoice = raw_input("> ")
=======
	print( "Welcome to my translation program!")
	print( "What would you like to do?")
	print( "A) Translate something to English")
	print( "B) Translate English to some other language")
	mychoice = input("> ")
>>>>>>> py2 to py3
	if mychoice == 'a':
		foreigntoEng()
	elif mychoice == 'b':
		transtolang()


def foreigntoEng():
<<<<<<< HEAD
	translate_client = translate.Client(api_key)
	print ("\n" * 100)
	print "Enter your foreign phrase below! "
	forphr = raw_input("> ")
	translation = translate_client.translate(forphr)
	for country, code in langcodes.iteritems():
		if code == translation['detectedSourceLanguage']:
			detcountry = country
	print "Working..."
	sleep(4)
	try:
		print "It looks like you said '%s' in %s." % (translation['translatedText'], detcountry.capitalize())
	except UnboundLocalError:
		print "Your text could not be translated. Please try again."
=======
	translate_client = translate.Client()
	print ("\n" * 100)
	print( "Enter your foreign phrase below! ")
	forphr = input("> ")
	translation = translate_client.translate(forphr)
	for country, code in langcodes.items():
		if code == translation['detectedSourceLanguage']:
			detcountry = country
	print( "Working...")
	sleep(4)
	try:
		print( "It looks like you said '%s' in %s." % (translation['translatedText'], detcountry.capitalize()))
	except UnboundLocalError:
		print( "Your text could not be translated. Please try again.")
>>>>>>> py2 to py3
	rerun()



def transtolang():
	# Enter the text to translate.
	print ("\n" * 100)
<<<<<<< HEAD
	print "Enter the word/sentence to be translated."
	text = raw_input('> ')
	# Enter the target language.
	print "Enter the language that you want this to be translated to."
	reqlang = raw_input('> ').lower().strip()
=======
	print( "Enter the word/sentence to be translated.")
	text = input('> ')
	# Enter the target language.
	print( "Enter the language that you want this to be translated to.")
	reqlang = input('> ').lower().strip()
>>>>>>> py2 to py3

	if reqlang in langcodes.keys():
		target = langcodes[reqlang]
		resultcode(text, target, reqlang)
		rerun()
	else:
<<<<<<< HEAD
		print "Your language is not supported in this program."
		print "Please try again!"
=======
		print( "Your language is not supported in this program.")
		print( "Please try again!")
>>>>>>> py2 to py3
		sleep(3)
		transtolang()


if __name__ == '__main__':
	mainmenu()
