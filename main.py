"""
Daily Sales Sheet Main Script
Coordinates the creation of Excel templates, sample data generation, and analysis.
"""

import os
import sys
from datetime import datetime


def check_dependencies():
    """Check if required packages are installed."""
    required_packages = ['pandas', 'openpyxl', 'matplotlib', 'seaborn', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for pkg in missing_packages:
            print(f"  - {pkg}")
        print("\nPlease install missing packages using:")
        print("pip install -r requirements.txt")
        return False
    
    return True


def create_excel_template():
    """Create Excel template with formulas and formatting."""
    try:
        from python_scripts.create_excel_template import SalesSheetCreator
        
        print("Creating Excel template...")
        creator = SalesSheetCreator()
        creator.create_sales_entry_sheet()
        creator.create_daily_summary_sheet()
        creator.create_product_analysis_sheet()
        creator.create_charts_sheet()
        
        template_path = creator.save_template()
        print(f"✓ Excel template created: {template_path}")
        return template_path
        
    except Exception as e:
        print(f"Error creating Excel template: {e}")
        return None


def generate_sample_data():
    """Generate sample sales data for testing."""
    try:
        from python_scripts.generate_sample_data import SampleDataGenerator
        
        print("Generating sample sales data...")
        generator = SampleDataGenerator()
        filepath = generator.generate_and_save(days=30)
        print(f"✓ Sample data generated: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"Error generating sample data: {e}")
        return None


def run_sales_analysis():
    """Run sales analysis and generate reports."""
    try:
        from python_scripts.sales_analyzer import SalesAnalyzer
        
        # First check if we have sample data to analyze
        sample_file = "sample_data/sample_sales_data.xlsx"
        if not os.path.exists(sample_file):
            print("No sample data found. Generating sample data first...")
            generate_sample_data()
        
        print("Running sales analysis...")
        analyzer = SalesAnalyzer(sample_file)
        analyzer.load_sales_data()
        report = analyzer.generate_sales_report()
        
        print("✓ Sales analysis complete!")
        print("\nGenerated visualizations:")
        viz_dir = "visualizations"
        if os.path.exists(viz_dir):
            for file in os.listdir(viz_dir):
                if file.endswith(('.png', '.jpg', '.txt')):
                    print(f"  - {os.path.join(viz_dir, file)}")
        
        return True
        
    except Exception as e:
        print(f"Error running sales analysis: {e}")
        return False


def launch_gui():
    """Launch the GUI application."""
    try:
        import tkinter as tk
        from gui_app import SalesSheetGUI
        
        print("Starting GUI application...")
        root = tk.Tk()
        app = SalesSheetGUI(root)
        
        # Center the window
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")
        
        root.mainloop()
        
    except ImportError:
        print("GUI not available. Please ensure tkinter is installed.")
    except Exception as e:
        print(f"Error launching GUI: {e}")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("     DAILY SALES SHEET MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Create Excel Template")
    print("2. Generate Sample Data")
    print("3. Run Sales Analysis")
    print("4. Complete Setup (All Steps)")
    print("5. View Project Information")
    print("6. Launch GUI Application")
    print("7. Exit")
    print("="*50)


def view_project_info():
    """Display project information and instructions."""
    print("\n" + "="*50)
    print("         PROJECT INFORMATION")
    print("="*50)
    
    print("\nProject Structure:")
    print("├── main.py                          # Main application entry point")
    print("├── gui_app.py                       # Tkinter GUI application")
    print("├── launch_gui.py                    # Direct GUI launcher")
    print("├── README.md                        # Project overview and instructions")
    print("├── requirements.txt                 # Python dependencies")
    print("├── .github/")
    print("│   └── copilot-instructions.md      # AI coding instructions")
    print("├── .vscode/")
    print("│   └── tasks.json                   # VS Code tasks configuration")
    print("├── .venv/                           # Python virtual environment")
    print("├── excel_templates/")
    print("│   └── daily_sales_sheet.xlsx       # Excel template with formulas")
    print("├── python_scripts/")
    print("│   ├── create_excel_template.py     # Excel template generator")
    print("│   ├── generate_sample_data.py      # Sample data generator")
    print("│   └── sales_analyzer.py            # Data analysis and visualization")
    print("├── sample_data/")
    print("│   └── sample_sales_data.xlsx       # Generated sample data")
    print("├── visualizations/")
    print("│   ├── daily_sales_trend.png        # Daily sales line chart")
    print("│   ├── product_performance.png      # Product bar chart")
    print("│   ├── category_distribution.png    # Category pie chart")
    print("│   ├── payment_methods.png          # Payment analysis")
    print("│   └── sales_analysis_report.txt    # Text report summary")
    print("└── documentation/")
    print("    ├── user_guide.md                # User instructions")
    print("    └── technical_docs.md             # Technical documentation")
    
    print("\nFeatures:")
    print("• GUI Application with intuitive tabbed interface")
    print("• Excel templates with automated formulas")
    print("• Data validation and dropdown lists")
    print("• Daily revenue calculations")
    print("• Product performance analysis")
    print("• Interactive charts and visualizations")
    print("• Sample data for testing")
    print("• Cross-platform compatibility (Windows, Mac, Linux)")
    print("• Command-line and GUI interfaces")
    
    print("\nFiles Created:")
    files_to_check = [
        "gui_app.py",
        "launch_gui.py",
        "excel_templates/daily_sales_sheet.xlsx",
        "sample_data/sample_sales_data.xlsx",
        "visualizations/daily_sales_trend.png",
        "visualizations/product_performance.png",
        "visualizations/category_distribution.png",
        "visualizations/payment_methods.png",
        "visualizations/sales_analysis_report.txt"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (not created yet)")
    
    print("\nNext Steps:")
    print("1. Launch GUI: python launch_gui.py (Recommended)")
    print("2. Or run 'Complete Setup' to create all files")
    print("3. Open Excel template to enter your sales data")
    print("4. Use Python scripts for advanced analysis")
    print("5. View generated charts in visualizations folder")
    print("6. Access comprehensive documentation in docs folder")


def complete_setup():
    """Run complete setup process."""
    print("\n" + "="*50)
    print("         COMPLETE SETUP")
    print("="*50)
    
    success = True
    
    # Step 1: Create Excel template
    print("\nStep 1: Creating Excel Template")
    if create_excel_template():
        print("✓ Excel template created successfully")
    else:
        print("✗ Failed to create Excel template")
        success = False
    
    # Step 2: Generate sample data
    print("\nStep 2: Generating Sample Data")
    if generate_sample_data():
        print("✓ Sample data generated successfully")
    else:
        print("✗ Failed to generate sample data")
        success = False
    
    # Step 3: Run analysis
    print("\nStep 3: Running Sales Analysis")
    if run_sales_analysis():
        print("✓ Sales analysis completed successfully")
    else:
        print("✗ Failed to run sales analysis")
        success = False
    
    if success:
        print("\n" + "="*50)
        print("🎉 SETUP COMPLETE! 🎉")
        print("="*50)
        print("\nYour Daily Sales Sheet system is ready!")
        print("\nWhat you can do now:")
        print("• Open excel_templates/daily_sales_sheet.xlsx")
        print("• Enter your sales data or use the sample data")
        print("• Run analysis scripts for insights")
        print("• View charts in the visualizations folder")
    else:
        print("\n⚠️  Setup completed with some errors.")
        print("Please check the error messages above.")


def main():
    """Main application loop."""
    print("Daily Sales Sheet Management System")
    print("Starting up...")
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease install required packages and try again.")
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                create_excel_template()
            elif choice == '2':
                generate_sample_data()
            elif choice == '3':
                run_sales_analysis()
            elif choice == '4':
                complete_setup()
            elif choice == '5':
                view_project_info()
            elif choice == '6':
                launch_gui()
            elif choice == '7':
                print("\nThank you for using the Daily Sales Sheet System!")
                print("Have a great day! 👋")
                break
            else:
                print("Invalid choice. Please enter a number from 1-7.")
                
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye! 👋")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
