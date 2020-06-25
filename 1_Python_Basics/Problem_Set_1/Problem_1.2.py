s = 'azcbobobeggbobhbobobakl'

count = 0
for i in range(len(s)):
	j = i + 3
	if s[i:j] == 'bob':
		count += 1

print('Number of times bob occurs is: ' + str(count))
