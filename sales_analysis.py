# ==========================================
# SALES DATA ANALYSIS PROJECT
# Created using Python and Matplotlib
# ==========================================

import matplotlib.pyplot as plt

# 1. Sales Dataset
products = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Keyboard",
    "Monitor",
    "Mouse",
    "Tablet",
    "Webcam"
]

categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Accessories",
    "Electronics",
    "Accessories"
]

units_sold = [10, 25, 40, 30, 15, 50, 12, 20]

prices = [
    50000,
    20000,
    1500,
    1000,
    12000,
    500,
    18000,
    2500
]

# 2. Calculate Product Revenue
revenue = []

for i in range(len(products)):
    product_revenue = units_sold[i] * prices[i]
    revenue.append(product_revenue)

# 3. Sales Summary
total_revenue = sum(revenue)
total_units = sum(units_sold)

top_index = revenue.index(max(revenue))

print("=" * 45)
print("         SALES DATA ANALYSIS")
print("=" * 45)

print("Total Revenue: Rs.", format(total_revenue, ","))
print("Total Units Sold:", total_units)

print(
    "Top Revenue Product:",
    products[top_index]
)

print(
    "Top Product Revenue: Rs.",
    format(revenue[top_index], ",")
)

print("-" * 45)
print("PRODUCT-WISE SALES REPORT")
print("-" * 45)

for i in range(len(products)):
    print(
        products[i],
        "| Units Sold:", units_sold[i],
        "| Revenue: Rs.", format(revenue[i], ",")
    )

# 4. Chart 1: Product-wise Revenue
plt.figure(figsize=(10, 6))

plt.bar(products, revenue)

plt.title("Product-wise Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("revenue_chart.png", dpi=300)
plt.show()

# 5. Chart 2: Units Sold by Product
plt.figure(figsize=(10, 6))

plt.bar(products, units_sold)

plt.title("Units Sold by Product")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("units_sold_chart.png", dpi=300)
plt.show()

# 6. Category-wise Revenue Analysis
category_revenue = {}

for i in range(len(categories)):
    category = categories[i]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue[i]

# 7. Chart 3: Category-wise Revenue
plt.figure(figsize=(8, 6))

plt.pie(
    category_revenue.values(),
    labels=category_revenue.keys(),
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Category-wise Revenue Distribution")
plt.tight_layout()
plt.savefig("category_revenue_chart.png", dpi=300)
plt.show()

# 8. Final Business Insights
print("=" * 45)
print("         BUSINESS INSIGHTS")
print("=" * 45)

for category, amount in category_revenue.items():
    print(
        category,
        "Revenue: Rs.",
        format(amount, ",")
    )

print("Analysis completed successfully!")
