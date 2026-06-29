import pandas as pd
import os

# -------------------------------------
# File Paths
# -------------------------------------

merged_file = "/opt/airflow/ecommerce/output/merged/merged_dataset.csv"

output_folder = "/opt/airflow/ecommerce/output/reports"
os.makedirs(output_folder, exist_ok=True)

# -------------------------------------
# Load Merged Dataset
# -------------------------------------

data = pd.read_csv(merged_file)

print("="*60)
print("BUSINESS ANALYSIS")
print("="*60)

# -------------------------------------
# Total Customers
# -------------------------------------

total_customers = data["customer_unique_id"].nunique()
print(f"\nTotal Customers : {total_customers}")

# -------------------------------------
# Total Orders
# -------------------------------------

total_orders = data["order_id"].nunique()
print(f"Total Orders : {total_orders}")

# -------------------------------------
# Total Revenue
# -------------------------------------

total_revenue = data["payment_value"].sum()
print(f"Total Revenue : {total_revenue:.2f}")

# -------------------------------------
# Average Payment
# -------------------------------------

average_payment = data["payment_value"].mean()
print(f"Average Payment : {average_payment:.2f}")

# -------------------------------------
# Top 10 Customer States
# -------------------------------------

print("\nTop 10 Customer States")
top_states = data["customer_state"].value_counts().head(10)
print(top_states)

# -------------------------------------
# Top 10 Customer Cities
# -------------------------------------

print("\nTop 10 Customer Cities")
top_cities = data["customer_city"].value_counts().head(10)
print(top_cities)

# -------------------------------------
# Order Status
# -------------------------------------

print("\nOrder Status")
order_status = data["order_status"].value_counts()
print(order_status)

# -------------------------------------
# Payment Methods
# -------------------------------------

print("\nPayment Methods")
payment_methods = data["payment_type"].value_counts()
print(payment_methods)

# -------------------------------------
# Revenue Statistics
# -------------------------------------

print("\nRevenue Statistics")
print(data["payment_value"].describe())

# -------------------------------------
# Monthly Revenue
# -------------------------------------

data["order_purchase_timestamp"] = pd.to_datetime(
    data["order_purchase_timestamp"]
)

monthly_revenue = (
    data.groupby(
        data["order_purchase_timestamp"].dt.to_period("M")
    )["payment_value"]
    .sum()
)

print("\nMonthly Revenue")
print(monthly_revenue)

# -------------------------------------
# Save Monthly Revenue
# -------------------------------------

monthly_file = os.path.join(
    output_folder,
    "Monthly_Revenue.csv"
)

monthly_revenue.to_csv(monthly_file)

print("\nMonthly Revenue saved successfully!")

# -------------------------------------
# Project Summary Report
# -------------------------------------

summary_file = os.path.join(
    output_folder,
    "Project_Summary.txt"
)

with open(summary_file, "w") as f:

    f.write("AUTOMATED DATA PIPELINE PROJECT\n")
    f.write("="*50 + "\n\n")

    f.write(f"Total Customers : {total_customers}\n")
    f.write(f"Total Orders : {total_orders}\n")
    f.write(f"Total Revenue : {total_revenue:.2f}\n")
    f.write(f"Average Payment : {average_payment:.2f}\n\n")

    f.write("Top 10 Customer States\n")
    f.write(str(top_states))

    f.write("\n\nTop 10 Customer Cities\n")
    f.write(str(top_cities))

    f.write("\n\nOrder Status\n")
    f.write(str(order_status))

    f.write("\n\nPayment Methods\n")
    f.write(str(payment_methods))

print("\n" + "="*60)
print("BUSINESS ANALYSIS COMPLETED SUCCESSFULLY")
print("="*60)

print("\nReports Folder:")
print(output_folder)
