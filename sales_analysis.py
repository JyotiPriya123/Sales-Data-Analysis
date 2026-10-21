import matplotlib.pyplot as plt

# Sales Data
products = [
    "Laptop", "Mobile", "Headphones",
    "Keyboard", "Monitor", "Mouse",
    "Tablet", "Webcam"
]

categories = [
    "Electronics", "Electronics", "Accessories",
    "Accessories", "Electronics", "Accessories",
    "Electronics", "Accessories"
]

units_sold = [10, 25, 40, 30, 15, 50, 12, 20]
prices = [50000, 20000, 1500, 1000, 12000, 500, 18000, 2500]

# Calculate Revenue
revenue = [
    units_sold[i] * prices[i]
    for i in range(len(products))
]

total_revenue = sum(revenue)
total_units = sum(units_sold)

print("=" * 40)
print("       SALES DATA ANALYSIS")
print("=" * 40)
print("Total Revenue: Rs.", total_revenue)
print("Total Units Sold:", total_units)

top_index = revenue.index(max(revenue))

print("Top Revenue Product:", products[top_index])
print("Top Product Revenue: Rs.", revenue[top_index])

# Chart 1: Product-wise Revenue
plt.figure(figsize=(10, 5))
plt.bar(products, revenue)
plt.title("Product-wise Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Chart 2: Units Sold
plt.figure(figsize=(10, 5))
plt.bar(products, units_sold)
plt.title("Units Sold by Product")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Chart 3: Category-wise Revenue
category_revenue = {}

for i in range(len(categories)):
    category = categories[i]
    category_revenue[category] = (
        category_revenue.get(category, 0) + revenue[i]
    )

plt.figure(figsize=(7, 7))
plt.pie(
    category_revenue.values(),
    labels=category_revenue.keys(),
    autopct="%1.1f%%"
)
plt.title("Category-wise Revenue Distribution")
plt.show()
