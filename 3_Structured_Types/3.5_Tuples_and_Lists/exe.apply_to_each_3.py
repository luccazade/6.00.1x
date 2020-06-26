def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def sqFunc(x):
	return x**2

applyToEach(testList, sqFunc)

print(testList)
