"""
================================================================================
    SUPERSTORE SALES ANALYSIS DASHBOARD
    Python with Data Science Internship Project
    
    Project: Category-wise Sales Analysis using Superstore Dataset
    Tools: Python, Pandas, Matplotlib, Seaborn, Plotly
    
    Dashboard Requirements:
    1. KPI (Key Performance Indicators)
    2. Segment wise Sales
    3. Ship Mode wise Sales
    4. Sub-Category wise Sales
    5. State wise Sales
================================================================================
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Set style for all plots
sns.set_theme(style="whitegrid", palette="husl")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 13

# Output directory for saving charts
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("       SUPERSTORE SALES ANALYSIS DASHBOARD")
print("       Python with Data Science Internship Project")
print("=" * 70)


# ============================================================
# 2. LOAD & EXPLORE DATA
# ============================================================
print("\n" + "=" * 70)
print("  STEP 1: DATA LOADING & EXPLORATION")
print("=" * 70)

# Load the dataset
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sample_Superstore_Data.xlsx")
df = pd.read_excel(DATA_PATH)

print(f"\n✅ Dataset loaded successfully!")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")

print(f"\n📋 Column Names & Data Types:")
print("-" * 50)
for col in df.columns:
    print(f"   {col:<20} → {df[col].dtype}")

print(f"\n📊 First 5 Rows:")
print(df.head().to_string())

print(f"\n📈 Statistical Summary (Numerical Columns):")
print(df.describe().to_string())


# ============================================================
# 3. DATA CLEANING & PREPROCESSING
# ============================================================
print("\n" + "=" * 70)
print("  STEP 2: DATA CLEANING & PREPROCESSING")
print("=" * 70)

# Check for missing values
print("\n🔍 Missing Values:")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "   No missing values found! ✅")

# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\n🔍 Duplicate Rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"   Removed {duplicates} duplicate rows ✅")
else:
    print("   No duplicates found! ✅")

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract useful date features
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.month_name()
df['Order Day'] = df['Order Date'].dt.day_name()
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

print(f"\n✅ Date features extracted (Year, Month, Day, Shipping Days)")
print(f"   Date Range: {df['Order Date'].min().strftime('%Y-%m-%d')} to {df['Order Date'].max().strftime('%Y-%m-%d')}")
print(f"   Years Covered: {sorted(df['Order Year'].unique())}")


# ============================================================
# 4. KPI — KEY PERFORMANCE INDICATORS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 3: KPI — KEY PERFORMANCE INDICATORS")
print("=" * 70)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()
avg_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100
avg_discount = df['Discount'].mean() * 100
avg_shipping_days = df['Shipping Days'].mean()

print(f"""
╔══════════════════════════════════════════════════════╗
║              KEY PERFORMANCE INDICATORS              ║
╠══════════════════════════════════════════════════════╣
║  💰 Total Sales         :  ${total_sales:>14,.2f}       ║
║  📈 Total Profit        :  ${total_profit:>14,.2f}       ║
║  📦 Total Quantity Sold :  {total_quantity:>14,}            ║
║  🛒 Total Orders        :  {total_orders:>14,}            ║
║  👥 Total Customers     :  {total_customers:>14,}            ║
║  💵 Avg Order Value     :  ${avg_order_value:>14,.2f}       ║
║  📊 Profit Margin       :  {profit_margin:>13.2f}%           ║
║  🏷️  Avg Discount        :  {avg_discount:>13.2f}%           ║
║  🚚 Avg Shipping Days   :  {avg_shipping_days:>13.1f}            ║
╚══════════════════════════════════════════════════════╝
""")

# --- KPI Dashboard Chart ---
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('📊 KEY PERFORMANCE INDICATORS (KPI) DASHBOARD', fontsize=22, fontweight='bold', y=1.02)

kpi_data = [
    ('Total Sales', f'${total_sales:,.0f}', '#2196F3'),
    ('Total Profit', f'${total_profit:,.0f}', '#4CAF50'),
    ('Total Orders', f'{total_orders:,}', '#FF9800'),
    ('Total Customers', f'{total_customers:,}', '#9C27B0'),
    ('Avg Order Value', f'${avg_order_value:,.0f}', '#F44336'),
    ('Profit Margin', f'{profit_margin:.1f}%', '#00BCD4'),
]

for idx, (title, value, color) in enumerate(kpi_data):
    row, col = divmod(idx, 3)
    ax = axes[row][col]
    ax.text(0.5, 0.5, value, transform=ax.transAxes, fontsize=36, fontweight='bold',
            ha='center', va='center', color=color)
    ax.text(0.5, 0.15, title, transform=ax.transAxes, fontsize=16,
            ha='center', va='center', color='#555555')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '01_KPI_Dashboard.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/01_KPI_Dashboard.png")


# ============================================================
# 5. SEGMENT WISE SALES ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 4: SEGMENT WISE SALES ANALYSIS")
print("=" * 70)

segment_sales = df.groupby('Segment').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Quantity=('Quantity', 'sum'),
    Total_Orders=('Order ID', 'nunique'),
    Avg_Discount=('Discount', 'mean')
).round(2).sort_values('Total_Sales', ascending=False)

segment_sales['Profit_Margin_%'] = ((segment_sales['Total_Profit'] / segment_sales['Total_Sales']) * 100).round(2)
segment_sales['Sales_%_Share'] = ((segment_sales['Total_Sales'] / total_sales) * 100).round(2)

print("\n📊 Segment-wise Sales Summary:")
print(segment_sales.to_string())

# --- Segment Wise Sales Charts ---
fig, axes = plt.subplots(1, 3, figsize=(20, 7))
fig.suptitle('📊 SEGMENT WISE SALES ANALYSIS', fontsize=20, fontweight='bold')

# Pie Chart - Sales Share
colors_segment = ['#2196F3', '#4CAF50', '#FF9800']
explode = (0.05, 0.05, 0.05)
axes[0].pie(segment_sales['Total_Sales'], labels=segment_sales.index, autopct='%1.1f%%',
            colors=colors_segment, explode=explode, shadow=True, startangle=140,
            textprops={'fontsize': 13, 'fontweight': 'bold'})
axes[0].set_title('Sales Distribution by Segment', fontsize=14, fontweight='bold')

# Bar Chart - Sales & Profit
x = np.arange(len(segment_sales.index))
width = 0.35
bars1 = axes[1].bar(x - width/2, segment_sales['Total_Sales'], width, label='Sales', color='#2196F3')
bars2 = axes[1].bar(x + width/2, segment_sales['Total_Profit'], width, label='Profit', color='#4CAF50')
axes[1].set_xlabel('Segment')
axes[1].set_ylabel('Amount ($)')
axes[1].set_title('Sales vs Profit by Segment', fontsize=14, fontweight='bold')
axes[1].set_xticks(x)
axes[1].set_xticklabels(segment_sales.index)
axes[1].legend()
axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))

# Bar Chart - Profit Margin
colors_margin = ['#4CAF50' if v > 0 else '#F44336' for v in segment_sales['Profit_Margin_%']]
bars3 = axes[2].bar(segment_sales.index, segment_sales['Profit_Margin_%'], color=colors_margin)
axes[2].set_xlabel('Segment')
axes[2].set_ylabel('Profit Margin (%)')
axes[2].set_title('Profit Margin by Segment', fontsize=14, fontweight='bold')
for bar, val in zip(bars3, segment_sales['Profit_Margin_%']):
    axes[2].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '02_Segment_Wise_Sales.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/02_Segment_Wise_Sales.png")


# ============================================================
# 6. SHIP MODE WISE SALES ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 5: SHIP MODE WISE SALES ANALYSIS")
print("=" * 70)

shipmode_sales = df.groupby('Ship Mode').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Quantity=('Quantity', 'sum'),
    Total_Orders=('Order ID', 'nunique'),
    Avg_Shipping_Days=('Shipping Days', 'mean')
).round(2).sort_values('Total_Sales', ascending=False)

shipmode_sales['Profit_Margin_%'] = ((shipmode_sales['Total_Profit'] / shipmode_sales['Total_Sales']) * 100).round(2)
shipmode_sales['Sales_%_Share'] = ((shipmode_sales['Total_Sales'] / total_sales) * 100).round(2)

print("\n🚚 Ship Mode-wise Sales Summary:")
print(shipmode_sales.to_string())

# --- Ship Mode Wise Sales Charts ---
fig, axes = plt.subplots(1, 3, figsize=(20, 7))
fig.suptitle('🚚 SHIP MODE WISE SALES ANALYSIS', fontsize=20, fontweight='bold')

# Donut Chart
colors_ship = ['#E91E63', '#3F51B5', '#009688', '#FF5722']
wedges, texts, autotexts = axes[0].pie(
    shipmode_sales['Total_Sales'], labels=shipmode_sales.index,
    autopct='%1.1f%%', colors=colors_ship, startangle=90,
    pctdistance=0.75, textprops={'fontsize': 11, 'fontweight': 'bold'}
)
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
axes[0].add_artist(centre_circle)
axes[0].set_title('Sales Distribution by Ship Mode', fontsize=14, fontweight='bold')

# Horizontal Bar Chart
bars = axes[1].barh(shipmode_sales.index, shipmode_sales['Total_Sales'], color=colors_ship)
axes[1].set_xlabel('Total Sales ($)')
axes[1].set_title('Total Sales by Ship Mode', fontsize=14, fontweight='bold')
axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
for bar, val in zip(bars, shipmode_sales['Total_Sales']):
    axes[1].text(val + 5000, bar.get_y() + bar.get_height()/2.,
                 f'${val:,.0f}', ha='left', va='center', fontweight='bold', fontsize=10)

# Avg Shipping Days
bars2 = axes[2].bar(shipmode_sales.index, shipmode_sales['Avg_Shipping_Days'],
                    color=colors_ship)
axes[2].set_xlabel('Ship Mode')
axes[2].set_ylabel('Average Shipping Days')
axes[2].set_title('Avg Shipping Days by Ship Mode', fontsize=14, fontweight='bold')
for bar, val in zip(bars2, shipmode_sales['Avg_Shipping_Days']):
    axes[2].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
                 f'{val:.1f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '03_ShipMode_Wise_Sales.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/03_ShipMode_Wise_Sales.png")


# ============================================================
# 7. SUB-CATEGORY WISE SALES ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 6: SUB-CATEGORY WISE SALES ANALYSIS")
print("=" * 70)

subcat_sales = df.groupby('Sub-Category').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Quantity=('Quantity', 'sum'),
    Total_Orders=('Order ID', 'nunique')
).round(2).sort_values('Total_Sales', ascending=False)

subcat_sales['Profit_Margin_%'] = ((subcat_sales['Total_Profit'] / subcat_sales['Total_Sales']) * 100).round(2)

print("\n📦 Sub-Category-wise Sales Summary:")
print(subcat_sales.to_string())

# --- Sub-Category Wise Sales Charts ---
fig, axes = plt.subplots(2, 2, figsize=(20, 14))
fig.suptitle('📦 SUB-CATEGORY WISE SALES ANALYSIS', fontsize=20, fontweight='bold')

# Top Sales Bar Chart
colors_sub = sns.color_palette("husl", len(subcat_sales))
bars1 = axes[0][0].barh(subcat_sales.index, subcat_sales['Total_Sales'], color=colors_sub)
axes[0][0].set_xlabel('Total Sales ($)')
axes[0][0].set_title('Sales by Sub-Category', fontsize=14, fontweight='bold')
axes[0][0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
axes[0][0].invert_yaxis()

# Profit Bar Chart (with negative highlighting)
profit_colors = ['#4CAF50' if v >= 0 else '#F44336' for v in subcat_sales['Total_Profit']]
bars2 = axes[0][1].barh(subcat_sales.index, subcat_sales['Total_Profit'], color=profit_colors)
axes[0][1].set_xlabel('Total Profit ($)')
axes[0][1].set_title('Profit by Sub-Category (🟢 Profit / 🔴 Loss)', fontsize=14, fontweight='bold')
axes[0][1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
axes[0][1].invert_yaxis()
axes[0][1].axvline(x=0, color='black', linewidth=0.8, linestyle='--')

# Quantity Bar Chart
bars3 = axes[1][0].barh(subcat_sales.index, subcat_sales['Total_Quantity'], color=colors_sub)
axes[1][0].set_xlabel('Total Quantity')
axes[1][0].set_title('Quantity Sold by Sub-Category', fontsize=14, fontweight='bold')
axes[1][0].invert_yaxis()

# Profit Margin Bar Chart
margin_colors = ['#4CAF50' if v >= 0 else '#F44336' for v in subcat_sales['Profit_Margin_%']]
bars4 = axes[1][1].barh(subcat_sales.index, subcat_sales['Profit_Margin_%'], color=margin_colors)
axes[1][1].set_xlabel('Profit Margin (%)')
axes[1][1].set_title('Profit Margin by Sub-Category', fontsize=14, fontweight='bold')
axes[1][1].invert_yaxis()
axes[1][1].axvline(x=0, color='black', linewidth=0.8, linestyle='--')
for bar, val in zip(bars4, subcat_sales['Profit_Margin_%']):
    axes[1][1].text(val + (0.5 if val >= 0 else -3), bar.get_y() + bar.get_height()/2.,
                    f'{val:.1f}%', ha='left' if val >= 0 else 'right', va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '04_SubCategory_Wise_Sales.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/04_SubCategory_Wise_Sales.png")


# ============================================================
# 8. STATE WISE SALES ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 7: STATE WISE SALES ANALYSIS")
print("=" * 70)

state_sales = df.groupby('State').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Orders=('Order ID', 'nunique')
).round(2).sort_values('Total_Sales', ascending=False)

state_sales['Profit_Margin_%'] = ((state_sales['Total_Profit'] / state_sales['Total_Sales']) * 100).round(2)

print("\n🗺️ Top 15 States by Sales:")
print(state_sales.head(15).to_string())

print("\n🔻 Bottom 5 States by Sales:")
print(state_sales.tail(5).to_string())

print("\n🔴 Loss-making States:")
loss_states = state_sales[state_sales['Total_Profit'] < 0]
print(loss_states.to_string() if len(loss_states) > 0 else "   None!")

# --- State Wise Sales Charts ---
fig, axes = plt.subplots(2, 2, figsize=(22, 16))
fig.suptitle('🗺️ STATE WISE SALES ANALYSIS', fontsize=20, fontweight='bold')

# Top 15 States by Sales
top_15 = state_sales.head(15)
colors_state = sns.color_palette("Blues_r", 15)
bars1 = axes[0][0].barh(top_15.index, top_15['Total_Sales'], color=colors_state)
axes[0][0].set_xlabel('Total Sales ($)')
axes[0][0].set_title('Top 15 States by Sales', fontsize=14, fontweight='bold')
axes[0][0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
axes[0][0].invert_yaxis()
for bar, val in zip(bars1, top_15['Total_Sales']):
    axes[0][0].text(val + 2000, bar.get_y() + bar.get_height()/2.,
                    f'${val:,.0f}', ha='left', va='center', fontsize=9)

# Top 15 States by Profit
top_profit = state_sales.sort_values('Total_Profit', ascending=False).head(15)
profit_colors = ['#4CAF50' if v >= 0 else '#F44336' for v in top_profit['Total_Profit']]
bars2 = axes[0][1].barh(top_profit.index, top_profit['Total_Profit'], color=profit_colors)
axes[0][1].set_xlabel('Total Profit ($)')
axes[0][1].set_title('Top 15 States by Profit', fontsize=14, fontweight='bold')
axes[0][1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
axes[0][1].invert_yaxis()

# Bottom 10 States (Loss-making)
bottom_10 = state_sales.sort_values('Total_Profit').head(10)
b_colors = ['#F44336' if v < 0 else '#4CAF50' for v in bottom_10['Total_Profit']]
bars3 = axes[1][0].barh(bottom_10.index, bottom_10['Total_Profit'], color=b_colors)
axes[1][0].set_xlabel('Total Profit ($)')
axes[1][0].set_title('Bottom 10 States by Profit (🔴 Loss States)', fontsize=14, fontweight='bold')
axes[1][0].invert_yaxis()
axes[1][0].axvline(x=0, color='black', linewidth=0.8, linestyle='--')
axes[1][0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))

# Top 15 States by Orders
top_orders = state_sales.sort_values('Total_Orders', ascending=False).head(15)
bars4 = axes[1][1].barh(top_orders.index, top_orders['Total_Orders'], color=sns.color_palette("Oranges_r", 15))
axes[1][1].set_xlabel('Total Orders')
axes[1][1].set_title('Top 15 States by Number of Orders', fontsize=14, fontweight='bold')
axes[1][1].invert_yaxis()

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '05_State_Wise_Sales.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/05_State_Wise_Sales.png")


# ============================================================
# 9. ADDITIONAL ANALYSIS — Category & Year-wise Trends
# ============================================================
print("\n" + "=" * 70)
print("  STEP 8: ADDITIONAL ANALYSIS")
print("=" * 70)

# Category wise Sales
category_sales = df.groupby('Category').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Quantity=('Quantity', 'sum')
).round(2).sort_values('Total_Sales', ascending=False)

print("\n📂 Category-wise Sales:")
print(category_sales.to_string())

# Year-wise Sales Trend
yearly_sales = df.groupby('Order Year').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Orders=('Order ID', 'nunique')
).round(2)

print("\n📅 Year-wise Sales Trend:")
print(yearly_sales.to_string())

# --- Additional Charts ---
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('📊 ADDITIONAL ANALYSIS', fontsize=20, fontweight='bold')

# Category Sales Pie
cat_colors = ['#E91E63', '#2196F3', '#4CAF50']
axes[0][0].pie(category_sales['Total_Sales'], labels=category_sales.index,
               autopct='%1.1f%%', colors=cat_colors, shadow=True, startangle=140,
               explode=(0.05, 0.05, 0.05), textprops={'fontsize': 13, 'fontweight': 'bold'})
axes[0][0].set_title('Sales by Category', fontsize=14, fontweight='bold')

# Year-wise Sales Trend Line
axes[0][1].plot(yearly_sales.index, yearly_sales['Total_Sales'], marker='o', linewidth=3,
                color='#2196F3', markersize=10, label='Sales')
axes[0][1].plot(yearly_sales.index, yearly_sales['Total_Profit'], marker='s', linewidth=3,
                color='#4CAF50', markersize=10, label='Profit')
axes[0][1].set_xlabel('Year')
axes[0][1].set_ylabel('Amount ($)')
axes[0][1].set_title('Year-wise Sales & Profit Trend', fontsize=14, fontweight='bold')
axes[0][1].legend(fontsize=12)
axes[0][1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
axes[0][1].set_xticks(yearly_sales.index)

# Month-wise Sales Heatmap Data
monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().unstack(fill_value=0)
sns.heatmap(monthly_sales, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[1][0],
            xticklabels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
axes[1][0].set_title('Monthly Sales Heatmap by Year', fontsize=14, fontweight='bold')
axes[1][0].set_ylabel('Year')

# Region wise Sales
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_colors = ['#E91E63', '#3F51B5', '#009688', '#FF5722']
bars = axes[1][1].bar(region_sales.index, region_sales.values, color=region_colors)
axes[1][1].set_xlabel('Region')
axes[1][1].set_ylabel('Total Sales ($)')
axes[1][1].set_title('Sales by Region', fontsize=14, fontweight='bold')
axes[1][1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda val, _: f'${val:,.0f}'))
for bar, val in zip(bars, region_sales.values):
    axes[1][1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 5000,
                    f'${val:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '06_Additional_Analysis.png'), dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/06_Additional_Analysis.png")


# ============================================================
# 10. KEY INSIGHTS & CONCLUSIONS
# ============================================================
print("\n" + "=" * 70)
print("  STEP 9: KEY INSIGHTS & CONCLUSIONS")
print("=" * 70)

top_segment = segment_sales['Total_Sales'].idxmax()
top_shipmode = shipmode_sales['Total_Sales'].idxmax()
top_subcat = subcat_sales['Total_Sales'].idxmax()
top_state = state_sales['Total_Sales'].idxmax()
worst_subcat = subcat_sales['Total_Profit'].idxmin()
top_category = category_sales['Total_Sales'].idxmax()

loss_subcats = subcat_sales[subcat_sales['Total_Profit'] < 0].index.tolist()

print(f"""
╔══════════════════════════════════════════════════════════════════╗
║                    KEY INSIGHTS & CONCLUSIONS                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  1. 💰 Total Business Revenue: ${total_sales:,.2f}              ║
║     with a Profit Margin of {profit_margin:.1f}%                ║
║                                                                 ║
║  2. 👥 Top Segment: "{top_segment}" leads with                  ║
║     ${segment_sales.loc[top_segment, 'Total_Sales']:,.2f} in sales     ║
║                                                                 ║
║  3. 🚚 Most Used Ship Mode: "{top_shipmode}"                   ║
║     (${shipmode_sales.loc[top_shipmode, 'Total_Sales']:,.2f} in sales) ║
║                                                                 ║
║  4. 📦 Top Sub-Category: "{top_subcat}"                        ║
║     (${subcat_sales.loc[top_subcat, 'Total_Sales']:,.2f} in sales)    ║
║                                                                 ║
║  5. 🗺️  Top State: "{top_state}"                                ║
║     (${state_sales.loc[top_state, 'Total_Sales']:,.2f} in sales)      ║
║                                                                 ║
║  6. 📂 Top Category: "{top_category}"                           ║
║     (${category_sales.loc[top_category, 'Total_Sales']:,.2f})         ║
║                                                                 ║
║  7. 🔴 Loss-making Sub-Categories: {loss_subcats}               ║
║     → Need to review pricing & discount strategy                ║
║                                                                 ║
║  8. 🔻 Worst Performing Sub-Category: "{worst_subcat}"          ║
║     (Profit: ${subcat_sales.loc[worst_subcat, 'Total_Profit']:,.2f})  ║
║                                                                 ║
╚══════════════════════════════════════════════════════════════════╝
""")

# Save summary to CSV
summary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_summary_report.csv")
segment_sales.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "segment_sales_report.csv"))
shipmode_sales.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "shipmode_sales_report.csv"))
subcat_sales.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "subcategory_sales_report.csv"))
state_sales.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "state_sales_report.csv"))

print("✅ CSV Reports Generated:")
print("   → segment_sales_report.csv")
print("   → shipmode_sales_report.csv")
print("   → subcategory_sales_report.csv")
print("   → state_sales_report.csv")

print("\n" + "=" * 70)
print("  ✅ PROJECT COMPLETED SUCCESSFULLY!")
print("  📊 All Charts saved in 'charts/' folder")
print("  📄 All CSV Reports generated")
print("=" * 70)
print("\n  Thank you! — Python with Data Science Internship Project\n")
