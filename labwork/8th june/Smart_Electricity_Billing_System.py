# Electricity consumption data
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Task 1: Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# Task 2: Highest consuming house
high_house = ""
high_units = 0

for house in units:
    if units[house] > high_units:
        high_units = units[house]
        high_house = house

print("\nHighest Consumption:")
print(high_house, "(", high_units, "units)", sep="")

# Task 3: Lowest consuming house
low_house = ""
low_units = list(units.values())[0]

for house in units:
    if units[house] < low_units:
        low_units = units[house]
        low_house = house

print("\nLowest Consumption:")
print(low_house, "(", low_units, "units)", sep="")

# Task 4: Total units consumed
total = 0

for house in units:
    total += units[house]

print("\nTotal Units Consumed:", total)

# Task 5: Create lists
low = []
medium = []
high = []

for house in units:
    value = units[house]

    if value < 200:
        low.append(house)
    elif value <= 400:
        medium.append(house)
    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# Task 6: Energy-saving campaign
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)
