def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    listOfKeys = []
    for i in aDict.keys():
        if aDict[i] == target:
            listOfKeys.append(i)
    numberOfKeys = len(listOfKeys)
    incKeys = []
    for i in range(numberOfKeys):
        minNow = min(listOfKeys)
        incKeys.append(minNow)
        listOfKeys.remove(minNow)
    return incKeys


dictExample = {1: 0,
               2: 0,
               5: 2,
               0: 0,
               -1: 0}

print(keysWithValue({}, 4))