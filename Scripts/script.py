import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import xlsxwriter

# Load transaction data
file_path = './data/transactions_sample.csv'
df = pd.read_csv(file_path)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Basic summary statistics
summary = df.groupby('Category')['Amount'].sum().sort_values()
print("\nTotal Spend by Category:")
print(summary)

# Monthly trend plot
monthly = df.groupby(['Month', 'Category'])['Amount'].sum().unstack().fillna(0)
monthly.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Monthly Spending Breakdown by Category')
plt.ylabel('Amount ($)')
plt.xlabel('Month')
plt.tight_layout()
plt.savefig('./data/monthly_spending_chart.png')
plt.show()

# Export analysis
summary.to_csv('./data/spend_by_category.csv')
