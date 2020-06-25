def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string

	returns: True if char is in aStr; False otherwise
	'''
	low = 0
	high = len(aStr)
	ans = (high + low)//2
	if ans == 0:
		return False
	else:
		if char == aStr[ans]:
			return True
		elif char > aStr[ans]:
			return isIn(char, aStr[ans:])
		else:
			return isIn(char, aStr[:ans])

print(isIn('k', 'abdfffffhknq'))