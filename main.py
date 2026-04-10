import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (7,4)

# ✅ Create folder
os.makedirs("images", exist_ok=True)

df = pd.read_csv("bank_data.csv")

df['job'] = df['job'].fillna('Unknown')
df['education'] = df['education'].fillna('Unknown')

bins = [18, 25, 35, 50, 65, 100]
labels = ['18-25', '26-35', '36-50', '51-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

print("Total Customers:", len(df))

# ✅ Save plots
sns.countplot(x='deposit', data=df)
plt.title("Deposit Subscription")
plt.savefig("images/deposit_plot.png")
plt.clf()

sns.countplot(x='age_group', data=df)
plt.title("Age Distribution")
plt.savefig("images/age_distribution.png")
plt.clf()

sns.countplot(y='job', data=df)
plt.title("Job Distribution")
plt.savefig("images/job_distribution.png")
plt.clf()
