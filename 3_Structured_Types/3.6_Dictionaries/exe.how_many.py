animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    count = 0
    for i in aDict:
        count += (len(aDict[i]))
    return count

print(how_many(animals))

