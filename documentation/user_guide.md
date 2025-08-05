# Daily Sales Sheet User Guide

## Overview
The Daily Sales Sheet system helps small shop owners track, analyze, and summarize their daily sales data using Excel templates and Python analysis tools.

## Getting Started

### 1. Installation
First, ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Quick Setup
Run the main script for an interactive setup:
```bash
python main.py
```

Choose option 4 "Complete Setup" to create all files automatically.

## Using the Excel Template

### Sales Entry Sheet
The main sheet where you record daily sales:

**Columns:**
- **Date**: Transaction date (format: YYYY-MM-DD)
- **Product Name**: Name of the item sold
- **Category**: Product category (dropdown: Food, Beverage, Snack, Dessert, Other)
- **Quantity Sold**: Number of items sold
- **Unit Price**: Price per item
- **Total Amount**: Automatically calculated (Quantity × Unit Price)
- **Payment Method**: How customer paid (dropdown: Cash, Credit Card, etc.)
- **Customer Type**: Customer category (dropdown: Regular, New, VIP, etc.)

### Features
- **Data Validation**: Dropdown menus prevent data entry errors
- **Automatic Calculations**: Total amounts calculated automatically
- **Date Validation**: Ensures proper date formats
- **Professional Formatting**: Clear, easy-to-read layout

### Daily Summary Sheet
Automatically calculates:
- Total daily sales
- Number of transactions
- Average transaction value
- Best-selling products

### Product Analysis Sheet
Tracks performance by product:
- Total quantity sold
- Total revenue
- Average sale price
- Sales frequency

## Data Entry Best Practices

### 1. Consistent Naming
- Use consistent product names (e.g., "Coffee" not "coffee" or "COFFEE")
- Standardize categories
- Use proper date formats

### 2. Regular Updates
- Enter sales data daily
- Review weekly summaries
- Check for data accuracy

### 3. Backup
- Save Excel files regularly
- Keep backup copies
- Export data periodically

## Using Python Analysis Tools

### Generate Sample Data
```bash
python python_scripts/generate_sample_data.py
```
Creates realistic sample sales data for testing.

### Create Excel Template
```bash
python python_scripts/create_excel_template.py
```
Generates a formatted Excel template with formulas.

### Run Sales Analysis
```bash
python python_scripts/sales_analyzer.py
```
Analyzes sales data and creates visualizations.

## Understanding the Reports

### Daily Sales Trend
- Line chart showing sales over time
- Identifies peak sales days
- Shows weekly/monthly patterns

### Product Performance
- Bar chart of top-selling products
- Revenue comparison by product
- Helps identify best performers

### Category Distribution
- Pie chart of sales by category
- Shows which product types sell best
- Guides inventory decisions

### Payment Method Analysis
- Shows customer payment preferences
- Helps plan payment processing needs
- Identifies cash vs. card trends

## Troubleshooting

### Common Issues

**Excel formulas not working:**
- Ensure data is in correct columns
- Check for empty cells in calculation range
- Verify date formats

**Python scripts failing:**
- Check that all packages are installed
- Ensure Excel file exists
- Verify file permissions

**Charts not generating:**
- Check that data exists in Excel file
- Ensure visualizations folder exists
- Verify data types are correct

### Getting Help
1. Check error messages for specific issues
2. Ensure all required packages are installed
3. Verify file paths are correct
4. Review sample data format

## Tips for Success

### 1. Start Simple
- Begin with basic product categories
- Add complexity gradually
- Focus on consistent data entry

### 2. Regular Analysis
- Review weekly reports
- Identify trends early
- Adjust inventory based on insights

### 3. Data Quality
- Train staff on proper data entry
- Regular data validation
- Clean up inconsistencies promptly

### 4. Business Insights
- Track seasonal patterns
- Monitor product performance
- Analyze customer preferences
- Plan promotions based on data

## Advanced Features

### Custom Categories
Modify dropdown lists in Excel:
1. Select data validation cell
2. Edit the list values
3. Apply to all relevant cells

### Additional Metrics
Add your own calculations:
- Profit margins
- Inventory turnover
- Customer frequency
- Seasonal adjustments

### Integration Options
- Import from POS systems
- Export to accounting software
- Connect with inventory management
- Automate with scheduling

## Support
For additional help or customizations, refer to the README.md file or check the Python script comments for technical details.

## GUI Application

### Launching the GUI
The project now includes a user-friendly graphical interface built with tkinter:

```bash
# Direct GUI launch
python launch_gui.py

# Or through the main menu
python main.py
# Then choose option 6: "Launch GUI Application"
```

### GUI Features

#### Main Tab
- **Quick Actions**: One-click buttons for all major operations
- **Project Status**: Real-time overview of created files
- **Progress Tracking**: Visual feedback during operations

#### Data Tab
- **Template Management**: Create and open Excel templates
- **Sample Data**: Generate custom data with specified parameters
- **Data Import**: Import existing Excel sales files
- **File Access**: Quick viewing of generated files

#### Analysis Tab
- **Analysis Engine**: Run complete sales analysis with one click
- **Results Display**: View detailed analysis output
- **Chart Gallery**: Browse and open all generated visualizations
- **Report Access**: Direct access to text reports

#### Settings Tab
- **System Check**: Verify all dependencies are installed
- **Project Info**: Complete overview of features and structure
- **Environment Details**: Python version and path information

### GUI Benefits
- **User-Friendly**: No command-line experience required
- **Visual Interface**: Intuitive tabs and clear navigation
- **Error Handling**: Helpful error messages and guidance
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **File Integration**: Direct file opening and system integration
