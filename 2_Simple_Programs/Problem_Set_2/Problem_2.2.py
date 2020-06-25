balance = 3926
annualInterestRate = 0.2


low = 0
high = balance
ans = (high + low) // 2

def check_end_year(bal, air, low):
	for i in range(12):
		remainingPreInt = bal - low
		bal = remainingPreInt * (1 + air / 12)
	result = round(bal, 2)
	return result

xx = check_end_year(balance, annualInterestRate, 0)

while xx > 0:
	low += 10
	xx = check_end_year(balance, annualInterestRate, low)

print('Lowest Payment: ' + str(low))