# 🧾 User Guide: Personal Finance Dashboard in Excel

Welcome to the **Personal Finance Dashboard in Excel**! This guide will walk you through using the dashboard efficiently—from data entry to insights.

---

## 🔧 Setup Instructions

### 1. Download the Dashboard

* Open `FinanceDashboard.xlsx` in Microsoft Excel (preferably 2016+ for best compatibility).

### 2. Input Transactions

* Navigate to the **Transactions** sheet.
* Enter the following:

  * **Date** (format: mm/dd/yyyy)
  * **Description** (e.g., "Groceries", "Netflix Subscription")
  * **Amount** (positive for income, negative for expenses)
  * **Category**: Select from the drop-down (predefined categories like Food, Rent, Transport)

### 3. Add/Modify Categories (Optional)

* Go to the **Categories** sheet to add new types or rename existing ones.
* These will auto-update the validation list in the Transactions sheet.

---

## 📊 Using the Dashboard

### 1. Filter by Month or Category

* Navigate to the **Dashboard** sheet.
* Use **slicers** or filters to:

  * View a specific month
  * Filter by category or transaction type

### 2. Review Key Visuals

* **Monthly Spending Chart**: Track spending patterns.
* **Income vs. Expense Gauge**: Quick glance at budget balance.
* **Category Breakdown Pie Chart**: Visualize your spending distribution.

---

## ⚙️ Behind the Scenes

* **Power Query**: Used to import, clean, and structure data.
* **PivotTables & Charts**: Feed data into visuals.
* **Conditional Formatting**: Highlights large or unusual expenses.
* **Named Ranges**: Ensure formulas scale as you grow your data.

---

## 💡 Tips

* Refresh PivotTables: Use `Data > Refresh All` after adding new transactions.
* Avoid overwriting formulas or pivot table areas.
* Back up your file periodically.

---

## 📩 Support

Need help or have suggestions? Reach out via [GitHub Issues](https://github.com/BillOchieng/Personal-Finance-Dashboard-in-Excel/issues) or connect on [LinkedIn](https://linkedin.com/in/).

Happy budgeting! 💰
