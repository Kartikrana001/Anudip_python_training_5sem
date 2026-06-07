num = input("Enter Number: ")

peak = -1

for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        peak = i
    else:
        break

if peak == -1 or peak == len(num) - 1:
    print("Not a Mountain Number")
else:
    flag = True

    for i in range(peak + 1, len(num)):
        if num[i] >= num[i - 1]:
            flag = False
            break

    if flag:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")
