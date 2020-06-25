varA = 1
varB = 1.2

if type(varA) == str or type(varB) ==  str:
	print('string involved')
elif varA > varB:
	print('bigger')
elif varA == varB:
	print('equal')
elif varA < varB:
	print('smaller')
else:
	None

