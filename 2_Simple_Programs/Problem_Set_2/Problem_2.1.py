def pay_over_year(bal, air, mpr):
	for i in range(12):
		remainingPreInt = bal * (1 - mpr)
		bal = remainingPreInt * (1 + air / 12)
	return round(bal, 2)


print('Remaining balance: ' + str(pay_over_year(balance, annualInterestRate, monthlyPaymentRate)))
