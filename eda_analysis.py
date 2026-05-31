import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset for Data Analytics (2).xlsx")

print("="*50)
print("DATASET INFO")
print("="*50)

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------
# Basic Statistics
# ---------------------------

print("\nBASIC STATISTICS")
print(df.describe())

print("\nMedian Values")
print(df.median(numeric_only=True))

# ---------------------------
# Product Trend
# ---------------------------

product_counts = df["Product"].value_counts()

print("\nTop Products")
print(product_counts)

plt.figure(figsize=(8,5))
product_counts.plot(kind="bar")
plt.title("Product Distribution")
plt.tight_layout()
plt.savefig("product_distribution.png")
plt.show()

# ---------------------------
# Order Status Trend
# ---------------------------

status_counts = df["OrderStatus"].value_counts()

plt.figure(figsize=(8,5))
status_counts.plot(kind="bar")
plt.title("Order Status Distribution")
plt.tight_layout()
plt.savefig("order_status_distribution.png")
plt.show()

# ---------------------------
# Outlier Detection
# ---------------------------

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower) |
    (df["TotalPrice"] > upper)
]

print("\nNumber of Outliers:", len(outliers))

plt.figure(figsize=(8,5))
plt.boxplot(df["TotalPrice"])
plt.title("Total Price Outliers")
plt.savefig("outliers_boxplot.png")
plt.show()

print("\nEDA Completed Successfully")