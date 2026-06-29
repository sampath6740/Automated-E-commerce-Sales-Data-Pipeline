import pandas as pd
import os

# -------------------------------------
# Input and Output Paths
# -------------------------------------

input_folder = "/opt/airflow/ecommerce/output/cleaned"
output_folder = "/opt/airflow/ecommerce/output/merged"

os.makedirs(output_folder, exist_ok=True)

# -------------------------------------
# Load Cleaned Data
# -------------------------------------

customers = pd.read_csv(
    os.path.join(input_folder, "customers_clean.csv")
)

orders = pd.read_csv(
    os.path.join(input_folder, "orders_clean.csv")
)

payments = pd.read_csv(
    os.path.join(input_folder, "payments_clean.csv")
)

print("=" * 60)
print("CLEANED DATA LOADED SUCCESSFULLY")
print("=" * 60)

# -------------------------------------
# Merge Customers and Orders
# -------------------------------------

customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

# -------------------------------------
# Merge with Payments
# -------------------------------------

final_data = pd.merge(
    customer_orders,
    payments,
    on="order_id",
    how="inner"
)

print("\nMerged Dataset Shape:")
print(final_data.shape)

print("\nMerged Dataset Columns:")
print(final_data.columns)

print("\nFirst 5 Records:")
print(final_data.head())

# -------------------------------------
# Save Merged Dataset
# -------------------------------------

output_file = os.path.join(
    output_folder,
    "merged_dataset.csv"
)

final_data.to_csv(
    output_file,
    index=False
)

print("\nMerged dataset saved successfully!")
print(output_file)
