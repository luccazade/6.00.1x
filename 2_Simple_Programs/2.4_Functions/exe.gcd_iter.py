def gcdIter(a, b):
	'''
	a, b: positive integers

	returns: a positive integer, the greatest common divisor of a & b.
	'''
	test = min(a, b)
	for i in range(test):
		if a % test == 0 and b % test == 0:
			break
		else:
			test -= 1
	return test

print(gcdIter(1,12))
