#!/usr/bin/env python3
"""
Quick Setup Verification Script
Verifies the project is ready and guides through first-time setup.
"""

import os
import sys
from datetime import datetime

def check_project_status():
    """Check current project status and what needs to be created."""
    print("🏪 Daily Sales Sheet - Project Status Check")
    print("=" * 50)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Location: {os.getcwd()}")
    print()
    
    # Files to check
    files_to_check = [
        ("Excel Template", "excel_templates/daily_sales_sheet.xlsx", "Create with: python python_scripts/create_excel_template.py"),
        ("Sample Data", "sample_data/sample_sales_data.xlsx", "Create with: python python_scripts/generate_sample_data.py"),
        ("Sales Trend Chart", "visualizations/daily_sales_trend.png", "Create with: python python_scripts/sales_analyzer.py"),
        ("Product Performance", "visualizations/product_performance.png", "Run analysis after creating data"),
        ("Category Distribution", "visualizations/category_distribution.png", "Run analysis after creating data"),
        ("Payment Methods", "visualizations/payment_methods.png", "Run analysis after creating data"),
        ("Analysis Report", "visualizations/sales_analysis_report.txt", "Run analysis after creating data")
    ]
    
    created_count = 0
    total_count = len(files_to_check)
    
    print("📋 FILE STATUS:")
    print("-" * 50)
    
    for name, path, instruction in files_to_check:
        if os.path.exists(path):
            print(f"✅ {name}: {path}")
            created_count += 1
        else:
            print(f"❌ {name}: Not created yet")
            print(f"   ➡️  {instruction}")
    
    print()
    print(f"📊 PROGRESS: {created_count}/{total_count} files created ({created_count/total_count*100:.0f}%)")
    
    # Recommendations
    print()
    print("🎯 RECOMMENDED NEXT STEPS:")
    print("-" * 50)
    
    if created_count == 0:
        print("1. 🚀 Start fresh! Run: python launch_gui.py")
        print("2. 📊 Click 'Complete Setup' to create everything")
        print("3. 📝 Begin entering your sales data")
    elif created_count < 3:
        print("1. 📊 Create Excel template first")
        print("2. 📝 Generate sample data to see examples")
        print("3. 🔍 Run analysis to see charts")
    else:
        print("1. ✨ Great! Most files are ready")
        print("2. 📝 Start entering your own sales data")
        print("3. 🔍 Re-run analysis with new data")
    
    print()
    print("💡 QUICK COMMANDS:")
    print("-" * 50)
    print("🖥️  Launch GUI:        python launch_gui.py")
    print("💻 Interactive Menu:  python main.py")
    print("📊 Create Template:   python python_scripts/create_excel_template.py")
    print("🎲 Generate Data:     python python_scripts/generate_sample_data.py")
    print("📈 Run Analysis:      python python_scripts/sales_analyzer.py")
    
    return created_count, total_count

def check_dependencies():
    """Check if required packages are available."""
    print()
    print("🔧 DEPENDENCY CHECK:")
    print("-" * 50)
    
    required_packages = ['pandas', 'openpyxl', 'matplotlib', 'seaborn', 'numpy', 'tkinter']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'tkinter':
                import tkinter
            else:
                __import__(package)
            print(f"✅ {package}: Available")
        except ImportError:
            print(f"❌ {package}: Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print()
        print("⚠️  MISSING DEPENDENCIES:")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print()
        print("✅ All dependencies are available!")
        return True

def main():
    """Main verification function."""
    print()
    
    # Check dependencies first
    deps_ok = check_dependencies()
    
    # Check project status
    created, total = check_project_status()
    
    print()
    print("🏁 SUMMARY:")
    print("-" * 50)
    
    if not deps_ok:
        print("❌ Install missing dependencies first")
    elif created == 0:
        print("🆕 Fresh project - ready for first setup!")
    elif created == total:
        print("✅ Complete setup - ready to use!")
    else:
        print(f"🔨 Partial setup - {total-created} files remaining")
    
    print()
    print("Happy sales tracking! 🎉")

if __name__ == "__main__":
    main()
