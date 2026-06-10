# Railway Reservation Seat Analyzer

seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Task 1: Count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# Task 2: Find first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1

# Task 3: Calculate occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    percentage = (booked / len(seats)) * 100
    return percentage

# Task 4: Display available seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")

# Function Calls
booked, available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage:", round(occupancy_percentage(seats), 2), "%")

print()
display_available_seats(seats)
