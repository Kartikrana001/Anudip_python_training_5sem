# Product sales data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# Task 1: Products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product in sales:
    if sales[product] > 20:
        print(product)

# Task 2: Best-selling product
best_product = ""
best_sales = 0

for product in sales:
    if sales[product] > best_sales:
        best_sales = sales[product]
        best_product = product

print("\nBest Selling Product:", best_product, "(", best_sales, ")", sep="")

# Task 3: Least-selling product
least_product = ""
least_sales = list(sales.values())[0]

for product in sales:
    if sales[product] < least_sales:
        least_sales = sales[product]
        least_product = product

print("Least Selling Product:", least_product, "(", least_sales, ")", sep="")

# Task 4: Total products sold
total = 0

for product in sales:
    total += sales[product]

print("Total Units Sold:", total)

# Task 5: Products requiring promotion
promotion = []

for product in sales:
    if sales[product] < 15:
        promotion.append(product)

print("Products Requiring Promotion:")
print(promotion)

# Task 6: Count products with sales between 10 and 30
count = 0

for product in sales:
    if 10 <= sales[product] <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)
