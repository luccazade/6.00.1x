low = 0
high = 100

print('Please think of a number between 0 and 100!')

def check():
	global ans
	ans = (high + low) // 2
	print('Is your secret number %s?' % (ans))
	question = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to " \
	           "indicate I guessed correctly. "
	guess = input(question)
	return guess

x = check()

while x != 'c':
	if x == 'h':
		high = ans
		x = check()
	elif x == 'l':
		low = ans
		x = check()
	else:
		print('Sorry, I did not understand your input.')
		x = check()

print('Game over. Your secret number was: %s' % (ans))