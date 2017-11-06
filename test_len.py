wordbank = ["beve", "bevo", "bevi"]
print( "Your choices are: ")
mult = ['A] ', 'B] ', 'C] ', 'D] ', 'E] ']
stack = list(zip(mult, wordbank))
for s in stack:
    print( s[0], s[1])
chosen = "A"
print(chosen)
print("Stack is", stack)
for s in stack:
	print(s)
	if chosen in s[0]:
		print( "You chose " + s[1] + "!")
		goodword = s[1]

def test_existence():
	assert goodword

