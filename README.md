# 📊 E-Commerce Sales Data Analysis Project

A comprehensive data cleaning and visualization project demonstrating key data science skills using Python, Pandas, and Matplotlib.

---

## 🎯 Project Overview

This project analyzes e-commerce sales data from January 2024, showcasing:
- **Data Cleaning**: Handling missing values, data type conversion
- **Data Analysis**: Aggregations, grouping, and statistical summaries
- **Data Visualization**: Multiple chart types for insights presentation

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical operations

---

## 📁 Project Structure

```
ecommerce-analysis/
│
├── sales_data.csv              # Raw dataset
├── main.py                 # Main analysis script
├── sales_analysis_dashboard.png # Output visualization
└── README.md                   # Project documentation
```

---

## 📊 Dataset Description

**Columns:**
- `date`: Transaction date
- `product`: Product name
- `category`: Product category (Electronics, Clothing)
- `city`: City where sale occurred
- `quantity`: Number of units sold
- `unit_price`: Price per unit (₹)

**Sample Size:** 14 transactions  
**Date Range:** January 1-7, 2024  
**Categories:** Electronics, Clothing  
**Cities:** Mumbai, Delhi, Bangalore, Pune

---

## 🔍 Analysis Steps

### 1. **Data Loading & Inspection**
- Loaded CSV data using Pandas
- Examined shape, columns, and data types
- Identified missing values

### 2. **Data Cleaning**
- Converted `date` column to datetime format
- Handled missing values in `quantity` (filled with median)
- Checked and removed duplicates
- Created `total_sales` column (quantity × unit_price)

### 3. **Data Analysis**
- Total sales by category
- Total sales by city
- Top-selling products
- Daily sales trends
- Average transaction value

### 4. **Data Visualization**
Created 6 different visualizations:
1. **Bar Chart** - Sales by Category
2. **Bar Chart** - Sales by City
3. **Histogram** - Distribution of Unit Prices
4. **Line Chart** - Daily Sales Trend
5. **Horizontal Bar Chart** - Sales by Product
6. **Pie Chart** - Category Distribution

---

## 📈 Key Insights

- **Total Revenue:** ₹33,900
- **Total Transactions:** 14
- **Best Selling Category:** Electronics (₹21,600)
- **Top City:** Mumbai (₹12,000)
- **Most Popular Product:** Headphones (₹9,000)
- **Average Transaction Value:** ₹2,421.43

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/piyush4sure/ecommerce-analysis.git
   cd ecommerce-analysis
   ```

2. **Install required packages:**
   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Run the analysis:**
   ```bash
   python analysis.py
   ```

4. **View the output:**
   - Check the console for analysis results
   - Open `sales_analysis_dashboard.png` for visualizations

---

## 💡 Skills Demonstrated

✅ Data cleaning and preprocessing  
✅ Handling missing values  
✅ Data type conversion  
✅ Pandas operations (groupby, aggregation, filtering)  
✅ Statistical analysis  
✅ Creating multiple visualization types  
✅ Professional code documentation  

---

## 📷 Sample Output

![Sales Analysis Dashboard](sales_analysis_dashboard.png)

---

## 🔮 Future Enhancements

- [ ] Add interactive visualizations using Plotly
- [ ] Implement seasonal trend analysis
- [ ] Add customer segmentation analysis
- [ ] Create predictive sales forecasting model
- [ ] Build interactive dashboard with Streamlit

---

## 👤 Author

**PIYUSH CHAUDHARY**  

- GitHub: [@piyush4sure](https://github.com/piyush4sure)


---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Dataset created for educational purposes
- Inspired by real-world e-commerce analytics challenges

---

**⭐ If you found this project helpful, please give it a star!**