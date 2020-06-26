animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
	if len(aDict) == 0:
		return None
	else:
		maxlen = max(aDict)
		return maxlen

print(biggest({}))
