import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ==========================================
# File Paths
# ==========================================

merged_file = "/opt/airflow/ecommerce/output/merged/merged_dataset.csv"

charts_folder = "/opt/airflow/ecommerce/output/charts"
os.makedirs(charts_folder, exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

data = pd.read_csv(merged_file)

print("=" * 60)
print("VISUALIZATION")
print("=" * 60)

# Convert date column
data["order_purchase_timestamp"] = pd.to_datetime(
    data["order_purchase_timestamp"]
)

# ==========================================
# Top 10 Customer States
# ==========================================

top_states = data["customer_state"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar")
plt.title("Top 10 Customer States")
plt.xlabel("State")
plt.ylabel("Customers")
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Top_10_Customer_States.png"))
plt.close()

print("✓ Top_10_Customer_States.png")

# ==========================================
# Order Status
# ==========================================

order_status = data["order_status"].value_counts()

plt.figure(figsize=(10,6))
order_status.plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Order_Status_Distribution.png"))
plt.close()

print("✓ Order_Status_Distribution.png")

# ==========================================
# Payment Method
# ==========================================

payment_method = data["payment_type"].value_counts()

plt.figure(figsize=(8,8))
payment_method.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Payment Method Distribution")
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Payment_Method_Distribution.png"))
plt.close()

print("✓ Payment_Method_Distribution.png")

# ==========================================
# Revenue Distribution
# ==========================================

plt.figure(figsize=(10,6))
data["payment_value"].plot(
    kind="hist",
    bins=30
)

plt.title("Revenue Distribution")
plt.xlabel("Payment Value")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Revenue_Distribution.png"))
plt.close()

print("✓ Revenue_Distribution.png")

# ==========================================
# Payment Installments
# ==========================================

installments = (
    data["payment_installments"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,6))
installments.plot(kind="bar")

plt.title("Payment Installments")
plt.xlabel("Installments")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Payment_Installments.png"))
plt.close()

print("✓ Payment_Installments.png")

# ==========================================
# Monthly Orders Trend
# ==========================================

monthly_orders = (
    data.groupby(
        data["order_purchase_timestamp"].dt.to_period("M")
    )
    .size()
)

monthly_orders.index = monthly_orders.index.astype(str)

plt.figure(figsize=(14,6))
monthly_orders.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Orders Trend")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(charts_folder,
                         "Monthly_Orders_Trend.png"))
plt.close()

print("✓ Monthly_Orders_Trend.png")

print("\n" + "=" * 60)
print("ALL CHARTS GENERATED SUCCESSFULLY")
print("=" * 60)

print("\nCharts saved to:")
print(charts_folder)
