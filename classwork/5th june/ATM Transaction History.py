transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposits = []
withdrawals = []

for t in transactions:
    balance += t

    if t > 0:
        deposits.append(t)
    else:
        withdrawals.append(t)

largest_deposit = deposits[0]
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d

largest_withdrawal = withdrawals[0]
for w in withdrawals:
    if w < largest_withdrawal:
        largest_withdrawal = w

print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
