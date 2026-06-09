second = int(input("Enter time in second : "))
#check second is negative
if(second < 0):
	exit("Time cannot be negative..... Exited")
hour = 0
minute = 0

#converting number of second into hours

if(second >= 3600):
	hour = second // 3600
	second = second % 3600

#converting into minute

if(second >= 60):
	minute = second // 60
	second = second % 60

print("Equivalent Time : ",hour," Hour ",minute," Minute ",second," second")
