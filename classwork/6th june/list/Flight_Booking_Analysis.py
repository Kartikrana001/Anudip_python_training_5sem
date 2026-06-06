bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

print("Confirmed Passengers:")
for b in bookings:
    if b[2] == "Confirmed":
        print(b[0], b[1])

delhi_count = 0
confirmed = 0
waiting = 0
cancelled = 0

waiting_list = []

delhi = 0
mumbai = 0
chennai = 0

for b in bookings:

    if b[1] == "Delhi":
        delhi_count += 1
        delhi += 1

    elif b[1] == "Mumbai":
        mumbai += 1

    elif b[1] == "Chennai":
        chennai += 1

    if b[2] == "Confirmed":
        confirmed += 1

    elif b[2] == "Waiting":
        waiting += 1
        waiting_list.append(b[0])

    elif b[2] == "Cancelled":
        cancelled += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

print("\nWaiting List:")
print(waiting_list)

print("\nMost Booked Destination:")

if delhi >= mumbai and delhi >= chennai:
    print("Delhi", delhi)

elif mumbai >= delhi and mumbai >= chennai:
    print("Mumbai", mumbai)

else:
    print("Chennai", chennai)
