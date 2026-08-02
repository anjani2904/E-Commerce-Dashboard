import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Sales": [15, 40, 25, 10, 20],
    "Price": [50000, 500, 1200, 8000, 2000]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Sales"] * df["Price"]

print("E-Commerce Sales Report")
print(df)

print("\nTotal Revenue:", df["Revenue"].sum())

top_product = df.loc[df["Revenue"].idxmax()]

print("\nTop Selling Product:")
print(top_product)

print("\nAverage Revenue:", df["Revenue"].mean())
