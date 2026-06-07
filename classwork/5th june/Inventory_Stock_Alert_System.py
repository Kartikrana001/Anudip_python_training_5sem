stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock = []
available = 0
healthy = []

for s in stock:
    if s == 0:
        out_of_stock += 1

    if s < 10:
        restock.append(s)

    if s > 0:
        available += 1

    if s >= 15:
        healthy.append(s)

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy)
