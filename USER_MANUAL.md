# 📋 Daily Sales Sheet - Quick User Manual

**For Shop Owners and Staff**

This guide shows you exactly how to track your daily sales and get business insights in just a few minutes each day.

## 🚀 First Time Setup (One Time Only)

### Step 1: Install the System
```bash
python launch_gui.py
```
Click the **"Complete Setup"** button. This creates your Excel file automatically.

### Step 2: Open Your Sales Sheet
- Find the file: `excel_templates/daily_sales_sheet.xlsx`
- Open it in Microsoft Excel
- Bookmark this file - you'll use it every day!

**That's it!** Your system is ready.

---

## � Daily Routine (5 Minutes Total)

### Morning (1 minute)
1. Open your Excel file
2. Scroll to today's date section
3. Ready to record sales!

### During Each Sale (30 seconds)
**Add a new row for each transaction:**

| Column | What to Enter | Example |
|--------|---------------|---------|
| **Date** | Today's date | 2024-01-15 |
| **Product** | Item name | "Coffee", "Sandwich" |
| **Category** | Choose from dropdown | Food, Beverage, Snacks |
| **Quantity** | How many sold | 2 |
| **Price** | Price per item | 3.50 |
| **Total** | *Calculates automatically* | 7.00 |
| **Payment** | Choose: Cash or Card | Cash |
| **Customer** | Choose: Regular, New, VIP | Regular |

**💡 Tip**: Use the dropdown menus to keep entries consistent!

### End of Day (3 minutes)
1. **Check your entries** - make sure everything looks right
2. **Run analysis**: 
   - Option A: `python launch_gui.py` → Analysis tab → "Run Analysis"
   - Option B: `python main.py` → Choose option 3
3. **View your results** in the `visualizations/` folder

---

## 📈 What You'll Get

### Daily Summary
- **Total Revenue**: How much money you made
- **Transaction Count**: Number of sales
- **Average Sale**: Revenue ÷ Transactions
- **Best Seller**: Your top product today

### Weekly Insights
- **Top 5 Products**: What makes you the most money
- **Busiest Days**: When to schedule more staff
- **Payment Trends**: How customers prefer to pay
- **Growth**: Compare this week to last week

### Business Charts
- Sales trends over time
- Product performance rankings
- Category breakdowns
- Customer type analysis

---

## 🛠️ Troubleshooting

### ❓ Excel file won't open
- **Solution**: Make sure you ran setup first: `python launch_gui.py` → "Complete Setup"
- **Location**: File is in `excel_templates/daily_sales_sheet.xlsx`

### ❓ Formulas not working
- **Check**: Data is in the correct columns (match the headers exactly)
- **Fix**: Look at sample data for the correct format

### ❓ No charts generated
- **Reason**: Need sales data first
- **Solution**: Enter some sales, then run analysis again

### ❓ Can't run analysis
- **Try**: `python main.py` instead of the GUI
- **Check**: Run `python check_status.py` to see what's missing

---

## 💡 Pro Tips for Shop Owners

### Data Entry Tips
- **Be Consistent**: Use the same product names every time
- **Use Dropdowns**: Prevents typos and keeps data clean
- **Daily Habit**: Enter sales as they happen, not at end of day
- **Double Check**: Quick review before running analysis

### Business Insights
- **Stock More Winners**: Your top 5 products should never run out
- **Schedule Smart**: Staff more people on your busiest days  
- **Payment Prep**: If customers prefer cash, ensure you have change
- **Weekly Reviews**: Look at trends every Sunday to plan the week

### Time Savers
- **Morning Setup**: Open Excel first thing, leave it open all day
- **Quick Codes**: Use short names like "ESP" for Espresso
- **End-of-Day**: Run analysis while you're closing the shop

---

## 📞 Quick Reference

### Commands You'll Use
```bash
python launch_gui.py        # Start the application
python check_status.py      # See what files exist
```

### File Locations
- **Your Sales Sheet**: `excel_templates/daily_sales_sheet.xlsx`
- **Your Charts**: `visualizations/` folder
- **Sample Data**: `sample_data/` folder (for reference)

### Daily Workflow
1. **Open Excel** → Enter sales → **Save file**
2. **Run analysis** → **Check charts** → **Plan tomorrow**

---

**Need More Help?** Check the `documentation/` folder for detailed guides.

**🎯 Remember**: 5 minutes a day of data entry gives you powerful business insights that can increase your profits!

