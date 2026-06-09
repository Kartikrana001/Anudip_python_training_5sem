# # 3. Smart Parking System
# Problem Statement
# Parking slots are represented as:
# slots = [1, 0, 1, 1, 0, 0, 1, 0]
# Where:
# * 1 = Occupied
# * 0 = Available
# Write a program to:
# * Count occupied and available slots.
# * Find the first available slot.
# * Display all available slot numbers.
# * Check whether parking occupancy exceeds 75%.
# Parking slots
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# Find first available slot
first_available = -1

for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i + 1   # Slot number starts from 1
        break

print("\nFirst Available Slot:", first_available)

# Display all available slot numbers
print("\nAvailable Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# Check parking occupancy percentage
occupancy = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy, "%")

if occupancy > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")
