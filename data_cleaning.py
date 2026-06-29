import pandas as pd
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

os.makedirs("/opt/airflow/ecommerce/output/charts", exist_ok=True)

# -------------------------------------
# Read Datasets
# -------------------------------------

customer_file = "/opt/airflow/ecommerce/input/customer.csv"
order_file = "/opt/airflow/ecommerce/input/order.csv"
payment_file = "/opt/airflow/ecommerce/input/payment.csv"

customers = pd.read_csv(customer_file)
orders = pd.read_csv(order_file)
payments = pd.read_csv(payment_file)

print("="*60)
print("DATASETS LOADED SUCCESSFULLY")
print("="*60)

print("\nCustomers Shape:", customers.shape)
print("Orders Shape:", orders.shape)
print("Payments Shape:", payments.shape)

# -------------------------------------
# Missing Values
# -------------------------------------

print("\n" + "="*60)
print("MISSING VALUES")
print("="*60)

print("\nCustomers")
print(customers.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

print("\nPayments")
print(payments.isnull().sum())

# -------------------------------------
# Duplicate Records
# -------------------------------------

print("\n" + "="*60)
print("DUPLICATE RECORDS")
print("="*60)

print("Customers:", customers.duplicated().sum())
print("Orders:", orders.duplicated().sum())
print("Payments:", payments.duplicated().sum())

# -------------------------------------
# Remove Duplicates
# -------------------------------------

customers = customers.drop_duplicates()
orders = orders.drop_duplicates()
payments = payments.drop_duplicates()

print("\nDuplicates Removed Successfully")

# -------------------------------------
# Dataset Information
# -------------------------------------

print("\n" + "="*60)
print("DATASET INFORMATION")
print("="*60)

print("\nCustomers")
print(customers.info())

print("\nOrders")
print(orders.info())

print("\nPayments")
print(payments.info())
# -------------------------------------
# Save Cleaned Datasets
# -------------------------------------

output_folder = "/opt/airflow/ecommerce/output/cleaned"
os.makedirs(output_folder, exist_ok=True)

customers.to_csv(
    os.path.join(output_folder, "customers_clean.csv"),
    index=False
)

orders.to_csv(
    os.path.join(output_folder, "orders_clean.csv"),
    index=False
)

payments.to_csv(
    os.path.join(output_folder, "payments_clean.csv"),
    index=False
)

print("\n" + "="*60)
print("CLEANED DATASETS SAVED SUCCESSFULLY")
print("="*60)
print(output_folder)
