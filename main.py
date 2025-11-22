import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

df = pd.read_csv('data/sales_data.csv')

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print(df)
print("\n")


print("=" * 60)
print("DATA INSPECTION")
print("=" * 60)

print("\n📊 Dataset Shape:", df.shape)
print(f"   - Rows: {df.shape[0]}")
print(f"   - Columns: {df.shape[1]}")

print("\n📋 Column Names:")
print(df.columns.tolist())

print("\n🔍 Data Types:")
print(df.dtypes)

print("\n❌ Missing Values:")
print(df.isnull().sum())

print("\n📈 Basic Statistics:")
print(df.describe())



print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)


df['date'] = pd.to_datetime(df['date'])
print("\n✅ Converted 'date' column to datetime format")


print(f"\n🔧 Missing values in 'quantity': {df['quantity'].isnull().sum()}")

median_quantity = df['quantity'].median()
df['quantity'].fillna(median_quantity, inplace=True)
print(f"   - Filled with median value: {median_quantity}")


duplicates = df.duplicated().sum()
print(f"\n🔍 Duplicate rows found: {duplicates}")
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("   - Duplicates removed!")


df['total_sales'] = df['quantity'] * df['unit_price']
print("\n✅ Created 'total_sales' column (quantity × unit_price)")

print("\n" + "=" * 60)
print("CLEANED DATASET")
print("=" * 60)
print(df)
print(f"\nFinal shape: {df.shape}")



print("\n" + "=" * 60)
print("DATA ANALYSIS")
print("=" * 60)


sales_by_category = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
print("\n💰 Total Sales by Category:")
print(sales_by_category)


sales_by_city = df.groupby('city')['total_sales'].sum().sort_values(ascending=False)
print("\n🏙️ Total Sales by City:")
print(sales_by_city)


sales_by_product = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
print("\n🏆 Top Selling Products:")
print(sales_by_product)

# Daily sales trend
daily_sales = df.groupby('date')['total_sales'].sum()
print("\n📅 Daily Sales Trend:")
print(daily_sales)




fig = plt.figure(figsize=(16, 10))
fig.suptitle('E-Commerce Sales Data Analysis Dashboard', fontsize=20, fontweight='bold', y=0.995)


ax1 = plt.subplot(2, 3, 1)
categories = sales_by_category.index
values = sales_by_category.values
colors = ['#FF6B6B', '#4ECDC4']
bars = ax1.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_title('Total Sales by Category', fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel('Category', fontsize=11, fontweight='bold')
ax1.set_ylabel('Total Sales (₹)', fontsize=11, fontweight='bold')
ax1.grid(axis='y', alpha=0.3, linestyle='--')

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'₹{int(height)}',
             ha='center', va='bottom', fontweight='bold', fontsize=10)


ax2 = plt.subplot(2, 3, 2)
cities = sales_by_city.index
city_values = sales_by_city.values
colors_city = ['#95E1D3', '#F38181', '#AA96DA', '#FCBAD3']
bars2 = ax2.bar(cities, city_values, color=colors_city, edgecolor='black', linewidth=1.5)
ax2.set_title('Total Sales by City', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('City', fontsize=11, fontweight='bold')
ax2.set_ylabel('Total Sales (₹)', fontsize=11, fontweight='bold')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
plt.xticks(rotation=45, ha='right')
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'₹{int(height)}',
             ha='center', va='bottom', fontweight='bold', fontsize=9)


ax3 = plt.subplot(2, 3, 3)
ax3.hist(df['unit_price'], bins=8, color='#FFA07A', edgecolor='black', linewidth=1.5, alpha=0.8)
ax3.set_title('Distribution of Unit Prices', fontsize=14, fontweight='bold', pad=10)
ax3.set_xlabel('Unit Price (₹)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax3.grid(axis='y', alpha=0.3, linestyle='--')


ax4 = plt.subplot(2, 3, 4)
ax4.plot(daily_sales.index, daily_sales.values, marker='o', linewidth=2.5, 
         markersize=8, color='#FF6B6B', markerfacecolor='#FFD93D', 
         markeredgecolor='black', markeredgewidth=1.5)
ax4.set_title('Daily Sales Trend', fontsize=14, fontweight='bold', pad=10)
ax4.set_xlabel('Date', fontsize=11, fontweight='bold')
ax4.set_ylabel('Total Sales (₹)', fontsize=11, fontweight='bold')
ax4.grid(True, alpha=0.3, linestyle='--')
plt.xticks(rotation=45, ha='right')

ax4.fill_between(daily_sales.index, daily_sales.values, alpha=0.3, color='#FF6B6B')


ax5 = plt.subplot(2, 3, 5)
products = sales_by_product.index
product_values = sales_by_product.values
colors_product = ['#A8E6CF', '#FFD3B6', '#FFAAA5', '#FF8B94']
bars5 = ax5.barh(products, product_values, color=colors_product, edgecolor='black', linewidth=1.5)
ax5.set_title('Sales by Product', fontsize=14, fontweight='bold', pad=10)
ax5.set_xlabel('Total Sales (₹)', fontsize=11, fontweight='bold')
ax5.set_ylabel('Product', fontsize=11, fontweight='bold')
ax5.grid(axis='x', alpha=0.3, linestyle='--')
for i, bar in enumerate(bars5):
    width = bar.get_width()
    ax5.text(width, bar.get_y() + bar.get_height()/2.,
             f'₹{int(width)}',
             ha='left', va='center', fontweight='bold', fontsize=9, 
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black', linewidth=1))


ax6 = plt.subplot(2, 3, 6)
category_counts = df.groupby('category').size()
colors_pie = ['#FF6B6B', '#4ECDC4']
explode = (0.05, 0.05)
wedges, texts, autotexts = ax6.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
                                     colors=colors_pie, explode=explode, startangle=90,
                                     textprops={'fontsize': 11, 'fontweight': 'bold'},
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 2})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)
ax6.set_title('Transaction Distribution by Category', fontsize=14, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✅ Visualizations saved as 'sales_analysis_dashboard.png'")
plt.show()



print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print(f"\n📊 Total Revenue: ₹{df['total_sales'].sum():.2f}")
print(f"📦 Total Transactions: {len(df)}")
print(f"🏆 Best Selling Category: {sales_by_category.idxmax()} (₹{sales_by_category.max()})")
print(f"🏙️ Top City: {sales_by_city.idxmax()} (₹{sales_by_city.max()})")
print(f"⭐ Most Popular Product: {sales_by_product.idxmax()} (₹{sales_by_product.max()})")
print(f"💵 Average Transaction Value: ₹{df['total_sales'].mean():.2f}")

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY! ✅")
print("=" * 60)