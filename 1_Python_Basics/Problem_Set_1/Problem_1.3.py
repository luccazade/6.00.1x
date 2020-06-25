s = 'abcbcd'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = []
for x in range(len(s)):
	count.append(0)
	if x >= len(s) - 1:
		count[x] = 0
		break
	else:
		j = x
		while alphabet.index(s[j]) <= alphabet.index(s[j + 1]):
			count[x] += 1
			j += 1
			if j == len(s) -1:
				break

maxLength = max(count)
maxIndex = count.index(maxLength)

string = s[maxIndex:maxIndex + maxLength + 1]

print('Longest substring in alphabetical order is: ' + string)