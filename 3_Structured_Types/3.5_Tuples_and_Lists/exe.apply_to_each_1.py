def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def absFunc(x):
	return abs(x)

applyToEach(testList, absFunc)

print(testList)