def iterPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0

	returns: int or float, base^exp
	'''
	answer = 1
	for i in range(exp):
		answer = answer * base
	return answer

print(iterPower(3,4))