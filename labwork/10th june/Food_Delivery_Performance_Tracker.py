# Food Delivery Performance Tracker

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Task 1: Find fastest delivery
def fastest_delivery(times):
    return min(times)

# Task 2: Find delayed orders
def delayed_orders(times):
    delayed = []

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed

# Task 3: Calculate average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# Task 4: Display delivery categories
def delivery_category(times):
    print("Categories:")

    for time in times:
        if time <= 30:
            print(time, "-> Fast")

        elif time <= 45:
            print(time, "-> Normal")

        else:
            print(time, "-> Delayed")

# Function Calls
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

print("\nAverage Delivery Time:")
print(round(average_delivery_time(delivery_time), 1), "minutes")

print()
delivery_category(delivery_time)
