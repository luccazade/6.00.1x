def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def plusFunc(x):
	return x +  1

applyToEach(testList, plusFunc)

print(testList)