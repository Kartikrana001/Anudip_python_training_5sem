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

destinations = {}

for b in bookings:

    if b[1] == "Delhi":
        delhi_count += 1

    if b[2] == "Confirmed":
        confirmed += 1
    elif b[2] == "Waiting":
        waiting += 1
        waiting_list.append(b[0])
    elif b[2] == "Cancelled":
        cancelled += 1

    if b[1] in destinations:
        destinations[b[1]] += 1
    else:
        destinations[b[1]] = 1

most_booked = ""
max_count = 0

for city in destinations:
    if destinations[city] > max_count:
        max_count = destinations[city]
        most_booked = city

print("\nPassengers Travelling to Delhi:", delhi_count)

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

print("\nWaiting List:")
print(waiting_list)

print("\nMost Booked Destination:")
print(most_booked, max_count)
