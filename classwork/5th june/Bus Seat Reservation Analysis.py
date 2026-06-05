seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []
first_available = -1

for i in range(len(seats)):
    if seats[i] == 1:
        booked += 1
    else:
        available += 1
        available_seats.append(i + 1)

        if first_available == -1:
            first_available = i + 1

occupancy = (booked * 100) / len(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
