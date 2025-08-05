# 🏪 Daily Sales Sheet for Small Shops

**Automated sales tracking system that turns your daily transactions into business insights.**

Perfect for coffee shops, convenience stores, restaurants, and any small retail business.

## ⚡ Quick Start (2 Minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch GUI
python launch_gui.py

# 3. Click "Complete Setup"
# 4. Start recording sales!
```

## 🎯 What This System Does

- **Daily Operations**: 30-second transaction entry with auto-calculations
- **Business Intelligence**: Identify best sellers, peak days, customer patterns
- **Automated Reports**: Revenue summaries, product rankings, trend charts
- **Professional Records**: Clean data for taxes, loans, business decisions

## 📊 Daily Workflow

1. **Morning**: Open Excel template, verify yesterday's entries
2. **During Sales**: Enter transactions (Product, Quantity, Price, Payment method)
3. **End of Day**: Run analysis for daily summary and insights
4. **Weekly**: Review trends, plan inventory and promotions

## 🔧 Installation

### Requirements
- Python 3.8+
- Microsoft Excel (2016+)

### Setup
```bash
pip install -r requirements.txt
python launch_gui.py  # Start with GUI
# OR
python main.py        # Start with CLI menu
```

## 📁 Project Structure

```
├── main.py                    # CLI application entry point
├── launch_gui.py              # GUI launcher
├── gui_app.py                 # Tkinter GUI interface
├── USER_MANUAL.md             # Quick user guide for shopkeepers
├── python_scripts/
│   ├── create_excel_template.py    # Excel template generator
│   ├── generate_sample_data.py     # Sample data for testing
│   └── sales_analyzer.py           # Data analysis & charts
├── excel_templates/           # Generated Excel files
├── sample_data/              # Test data
├── visualizations/           # Generated charts
└── documentation/            # Detailed guides
```

## � Usage Options

### 1. GUI Application (Recommended)
```bash
python launch_gui.py
```
- User-friendly interface
- Tabbed layout for different functions
- Visual progress indicators
- Easy template creation and analysis

### 2. Command Line Interface
```bash
python main.py
```
- Interactive menu system
- All features available
- Great for automation/scripting

### 3. Individual Scripts
```bash
python python_scripts/create_excel_template.py  # Create template
python python_scripts/generate_sample_data.py   # Generate test data
python python_scripts/sales_analyzer.py         # Run analysis
```

## 📈 Business Benefits

- **Increase Profits**: Stock more of what sells best
- **Save Time**: Automated calculations and reports  
- **Better Decisions**: Data-driven inventory and staffing
- **Professional Records**: Clean books for accounting
- **Growth Tracking**: Monitor business progress over time

## 🆘 Quick Help

```bash
python check_status.py     # Check what's been created
```

**Common Issues:**
- **Excel won't open**: Check file path in `excel_templates/`
- **No charts generated**: Need sales data first, then run analysis
- **GUI issues**: Try `python main.py` instead

**For detailed instructions**: See `USER_MANUAL.md` and `documentation/`
# sales-shop
