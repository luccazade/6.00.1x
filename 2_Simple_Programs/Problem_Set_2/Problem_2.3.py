balance = 999999
annualInterestRate = 0.18

epsilon = 0.005
low = balance / 12
high = ((balance * (1+ annualInterestRate)**12) / 12)
ans = (high + low) / 2

def check_end_year(bal, air, test):
	for i in range(12):
		remainingPreInt = bal - test
		bal = remainingPreInt * (1 + air / 12)
	return bal

xx = check_end_year(balance, annualInterestRate, ans)

while abs(xx - 0) > epsilon:
	if xx > 0:
		low = ans
		ans = (high + low) / 2
		xx = check_end_year(balance, annualInterestRate, ans)
	else:
		high = ans
		ans = (high + low) / 2
		xx = check_end_year(balance, annualInterestRate, ans)

print('Lowest Payment: ' + str(round(ans, 2)))