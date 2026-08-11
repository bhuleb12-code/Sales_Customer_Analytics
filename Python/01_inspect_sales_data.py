import pandas as pd

customers = pd.read_csv("../Data/customers.csv")

print(customers)


print("\nRows:", len(customers))
print("Columns:", len(customers.columns))
print("Countries:", customers["Country"].nunique())
print("Regions:", customers["Region"].nunique())

print("\nMissing values:")
print(customers.isna().sum())

print("\nDuplicate Customer IDs:", customers["CustomerID"].duplicated().sum())

products = pd.read_csv("../Data/products.csv")

print("\nProducts:")
print(products)

print("\nProduct rows:", len(products))
print("Product categories:", products["Category"].nunique())
print("Missing product values:")
print(products.isna().sum())
print("\nDuplicate Product IDs:", products["ProductID"].duplicated().sum())

orders = pd.read_csv("../Data/orders.csv")

print("\nOrders:")
print(orders)

print("\nOrder rows:", len(orders))
print("Missing order values:")
print(orders.isna().sum())
print("\nDuplicate Order IDs:", orders["OrderID"].duplicated().sum())

missing_customers = orders[
    ~orders["CustomerID"].isin(customers["CustomerID"])
]

print("\nOrders with invalid Customer IDs:", len(missing_customers))

order_details = pd.read_csv("../Data/order_details.csv")

print("\nOrder Details:")
print(order_details)

print("\nOrder detail rows:", len(order_details))
print("Missing order detail values:")
print(order_details.isna().sum())

print("\nDuplicate Order Detail IDs:", order_details["OrderDetailID"].duplicated().sum())

invalid_orders = order_details[
    ~order_details["OrderID"].isin(orders["OrderID"])
]

invalid_products = order_details[
    ~order_details["ProductID"].isin(products["ProductID"])
]

print("\nOrder details with invalid Order IDs:", len(invalid_orders))
print("Order details with invalid Product IDs:", len(invalid_products))