s = 'azcbobobegghakl'

vowels = ['a', 'e', 'i', 'o', 'u']
noVowels = 0
for i in s:
	if i in vowels:
		noVowels += 1

print('Number of vowels: ' + str(noVowels))
