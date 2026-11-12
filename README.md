# 🏪 Superstore Sales Analysis Dashboard
## Python with Data Science Internship Project

---

## 📋 Project Overview

This project analyzes the **Superstore Sales Dataset** to build a comprehensive Sales Dashboard using Python and Data Science tools. The dashboard covers all 5 required KPIs as per the internship requirements.

---

## 📌 Requirements Covered

| # | Requirement | Status |
|---|-------------|--------|
| 1 | KPI (Key Performance Indicators) | ✅ Done |
| 2 | Segment wise Sales | ✅ Done |
| 3 | Ship Mode wise Sales | ✅ Done |
| 4 | Sub-Category wise Sales | ✅ Done |
| 5 | State wise Sales | ✅ Done |

---

## 📊 Dataset Information

| Property | Value |
|----------|-------|
| File | Sample_Superstore_Data.xlsx |
| Total Rows | 9,994 |
| Total Columns | 21 |
| Date Range | Jan 2014 – Dec 2017 |
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Total Customers | 793 |

---

## 🛠️ Tools & Technologies Used

| Library | Purpose |
|---------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data loading, cleaning, analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization & charts |
| **Seaborn** | Statistical visualizations |
| **OpenPyXL** | Reading Excel files |

---

## 📁 Project Structure

```
Superstore_Sales_Dashboard_Project/
│
├── 📄 Sample_Superstore_Data.xlsx        ← Raw dataset
├── 🐍 superstore_sales_analysis.py       ← Main Python script
├── 📓 Superstore_Sales_Dashboard.ipynb   ← Jupyter Notebook
├── 📖 README.md                          ← Project documentation
│
├── 📊 charts/                            ← All generated charts
│   ├── 01_KPI_Dashboard.png
│   ├── 02_Segment_Wise_Sales.png
│   ├── 03_ShipMode_Wise_Sales.png
│   ├── 04_SubCategory_Wise_Sales.png
│   ├── 05_State_Wise_Sales.png
│   └── 06_Additional_Analysis.png
│
├── 📄 segment_sales_report.csv           ← Segment analysis report
├── 📄 shipmode_sales_report.csv          ← Ship mode analysis report
├── 📄 subcategory_sales_report.csv       ← Sub-category analysis report
└── 📄 state_sales_report.csv             ← State analysis report
```

---

## 🔍 Key Insights

1. **💰 Revenue:** Total Sales = **$2,297,200.86** with **12.5% Profit Margin**
2. **👥 Top Segment:** `Consumer` leads with **50.6%** of total sales
3. **🚚 Top Ship Mode:** `Standard Class` dominates with **59.1%** of sales
4. **📦 Top Sub-Category:** `Phones` has highest sales (**$330,007.05**)
5. **🗺️ Top State:** `California` with **$457,687.63** in sales
6. **📂 Top Category:** `Technology` (**$836,154.03**)
7. **🔴 Loss Sub-Categories:** `Tables`, `Bookcases`, `Supplies` → Need pricing review
8. **🔻 Loss States:** Texas, Ohio, Illinois, Pennsylvania → Require strategic attention

---

## ▶️ How to Run

### Option 1: Run Python Script
```bash
python superstore_sales_analysis.py
```

### Option 2: Jupyter Notebook
```bash
jupyter notebook Superstore_Sales_Dashboard.ipynb
```

### Install Requirements
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

---

## 📊 Output Charts

| Chart | Description |
|-------|-------------|
| `01_KPI_Dashboard.png` | 6 KPI metric cards |
| `02_Segment_Wise_Sales.png` | Sales by Consumer/Corporate/Home Office |
| `03_ShipMode_Wise_Sales.png` | Sales by Standard/Second/First/Same Day |
| `04_SubCategory_Wise_Sales.png` | All 17 sub-categories analysis |
| `05_State_Wise_Sales.png` | State-level sales & profit map |
| `06_Additional_Analysis.png` | Category, year trend, monthly heatmap |

---

*Python with Data Science Internship Project*
