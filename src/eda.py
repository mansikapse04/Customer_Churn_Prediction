import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Remove missing values
df = df.dropna(subset=["TotalCharges"])

# Churn distribution
print("Churn Distribution:")
print(df["Churn"].value_counts())

# Plot churn distribution
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()


plt.savefig("results/customer_churn_distribution.png")



# Churn by Contract Type
contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print("\nChurn by Contract Type:")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("results/churn_by_contract.png")


# Churn by Internet Service
internet_churn = pd.crosstab(df["InternetService"], df["Churn"])

print("\nChurn by Internet Service:")
print(internet_churn)

internet_churn.plot(kind="bar")

plt.title("Customer Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("results/churn_by_internet_service.png")


# Monthly Charges by Churn
df.boxplot(column="MonthlyCharges", by="Churn")

plt.title("Monthly Charges by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.tight_layout()
plt.savefig("results/monthly_charges_by_churn.png")