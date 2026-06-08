# Temperature data
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Task 1: Cities above 40°C
print("Cities Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city)

# Task 2: Hottest city
hot_city = ""
hot_temp = 0

for city in temperature:
    if temperature[city] > hot_temp:
        hot_temp = temperature[city]
        hot_city = city

print("\nHottest City:", hot_city, "(", hot_temp, "°C)", sep="")

# Task 3: Coolest city
cool_city = ""
cool_temp = list(temperature.values())[0]

for city in temperature:
    if temperature[city] < cool_temp:
        cool_temp = temperature[city]
        cool_city = city

print("Coolest City:", cool_city, "(", cool_temp, "°C)", sep="")

# Task 4: Average temperature
total = 0

for city in temperature:
    total += temperature[city]

average = total / len(temperature)

print("Average Temperature:", average)

# Task 5: Pleasant cities
pleasant = []

for city in temperature:
    if temperature[city] < 35:
        pleasant.append(city)

print("Pleasant Cities:")
print(pleasant)

# Task 6: Cities between 35°C and 40°C
count = 0

for city in temperature:
    if 35 <= temperature[city] <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)
