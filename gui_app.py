"""
Daily Sales Sheet GUI Application
A tkinter-based graphical user interface for the Daily Sales Sheet management system.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import os
import sys
import threading
from datetime import datetime
import subprocess
from pathlib import Path


class SalesSheetGUI:
    """Main GUI application for Daily Sales Sheet management."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Sales Sheet Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.status_var = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        
        self.setup_gui()
        self.check_dependencies()
    
    def setup_gui(self):
        """Setup the main GUI components."""
        # Main title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill="x", pady=(0, 10))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="🏪 Daily Sales Sheet Management System",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title_label.pack(expand=True)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_main_tab()
        self.create_data_tab()
        self.create_analysis_tab()
        self.create_settings_tab()
        
        # Status bar
        self.create_status_bar()
    
    def create_main_tab(self):
        """Create the main control tab."""
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="🏠 Main")
        
        # Welcome section
        welcome_frame = tk.LabelFrame(main_frame, text="Welcome", font=("Arial", 12, "bold"))
        welcome_frame.pack(fill="x", padx=10, pady=10)
        
        welcome_text = """Welcome to the Daily Sales Sheet Management System!
This application helps small shop owners track, analyze, and summarize daily sales data."""
        
        tk.Label(welcome_frame, text=welcome_text, justify="left", wraplength=800).pack(pady=10)
        
        # Quick actions section
        actions_frame = tk.LabelFrame(main_frame, text="Quick Actions", font=("Arial", 12, "bold"))
        actions_frame.pack(fill="x", padx=10, pady=10)
        
        # Button frame
        button_frame = tk.Frame(actions_frame)
        button_frame.pack(pady=10)
        
        # Action buttons
        buttons = [
            ("📊 Create Excel Template", self.create_template, "#3498db"),
            ("📝 Generate Sample Data", self.generate_sample_data, "#2ecc71"),
            ("📈 Run Sales Analysis", self.run_analysis, "#e74c3c"),
            ("🔧 Complete Setup", self.complete_setup, "#9b59b6")
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 11, "bold"),
                bg=color,
                fg="white",
                width=20,
                height=2,
                relief="raised",
                borderwidth=2
            )
            btn.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="ew")
        
        # Configure grid weights
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Project status section
        status_frame = tk.LabelFrame(main_frame, text="Project Status", font=("Arial", 12, "bold"))
        status_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Status display
        self.status_text = scrolledtext.ScrolledText(
            status_frame,
            height=10,
            font=("Consolas", 10),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        self.status_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Refresh status button
        tk.Button(
            status_frame,
            text="🔄 Refresh Status",
            command=self.refresh_status,
            font=("Arial", 10),
            bg="#17a2b8",
            fg="white"
        ).pack(pady=5)
        
        # Initial status load
        self.refresh_status()
    
    def create_data_tab(self):
        """Create the data management tab."""
        data_frame = ttk.Frame(self.notebook)
        self.notebook.add(data_frame, text="📊 Data")
        
        # Excel template section
        template_frame = tk.LabelFrame(data_frame, text="Excel Template", font=("Arial", 12, "bold"))
        template_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(template_frame, text="Manage your Excel sales template:").pack(anchor="w", padx=10, pady=5)
        
        template_buttons = tk.Frame(template_frame)
        template_buttons.pack(pady=10)
        
        tk.Button(
            template_buttons,
            text="📋 Create New Template",
            command=self.create_template,
            bg="#3498db",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=5)
        
        tk.Button(
            template_buttons,
            text="📂 Open Template",
            command=self.open_template,
            bg="#28a745",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=5)
        
        # Sample data section
        sample_frame = tk.LabelFrame(data_frame, text="Sample Data", font=("Arial", 12, "bold"))
        sample_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(sample_frame, text="Generate and manage sample sales data:").pack(anchor="w", padx=10, pady=5)
        
        # Sample data controls
        sample_controls = tk.Frame(sample_frame)
        sample_controls.pack(pady=10)
        
        tk.Label(sample_controls, text="Days of data:").pack(side="left")
        self.days_var = tk.StringVar(value="30")
        days_entry = tk.Entry(sample_controls, textvariable=self.days_var, width=10)
        days_entry.pack(side="left", padx=5)
        
        tk.Button(
            sample_controls,
            text="🎲 Generate Data",
            command=self.generate_custom_data,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=10)
        
        tk.Button(
            sample_controls,
            text="👁️ View Data",
            command=self.view_sample_data,
            bg="#ffc107",
            fg="black",
            font=("Arial", 10)
        ).pack(side="left", padx=5)
        
        # Data import section
        import_frame = tk.LabelFrame(data_frame, text="Data Import", font=("Arial", 12, "bold"))
        import_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(import_frame, text="Import your existing sales data:").pack(anchor="w", padx=10, pady=5)
        
        tk.Button(
            import_frame,
            text="📁 Import Excel File",
            command=self.import_data,
            bg="#fd7e14",
            fg="white",
            font=("Arial", 10)
        ).pack(pady=10)
    
    def create_analysis_tab(self):
        """Create the analysis and reporting tab."""
        analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(analysis_frame, text="📈 Analysis")
        
        # Analysis controls
        controls_frame = tk.LabelFrame(analysis_frame, text="Analysis Controls", font=("Arial", 12, "bold"))
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        control_buttons = tk.Frame(controls_frame)
        control_buttons.pack(pady=10)
        
        tk.Button(
            control_buttons,
            text="🔍 Run Full Analysis",
            command=self.run_analysis,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            height=2
        ).pack(side="left", padx=10)
        
        tk.Button(
            control_buttons,
            text="📊 View Charts",
            command=self.view_charts,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            height=2
        ).pack(side="left", padx=10)
        
        # Results display
        results_frame = tk.LabelFrame(analysis_frame, text="Analysis Results", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Consolas", 10),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Chart list
        charts_frame = tk.LabelFrame(analysis_frame, text="Generated Charts", font=("Arial", 12, "bold"))
        charts_frame.pack(fill="x", padx=10, pady=10)
        
        self.charts_listbox = tk.Listbox(charts_frame, height=4)
        self.charts_listbox.pack(fill="x", padx=10, pady=10)
        self.charts_listbox.bind("<Double-Button-1>", self.open_chart)
        
        # Refresh charts list
        self.refresh_charts_list()
    
    def create_settings_tab(self):
        """Create the settings and configuration tab."""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️ Settings")
        
        # Dependencies section
        deps_frame = tk.LabelFrame(settings_frame, text="Dependencies", font=("Arial", 12, "bold"))
        deps_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Button(
            deps_frame,
            text="🔍 Check Dependencies",
            command=self.check_dependencies,
            bg="#17a2b8",
            fg="white",
            font=("Arial", 10)
        ).pack(pady=10)
        
        self.deps_text = scrolledtext.ScrolledText(
            deps_frame,
            height=8,
            font=("Consolas", 9),
            bg="#f8f9fa"
        )
        self.deps_text.pack(fill="x", padx=10, pady=10)
        
        # Project info section
        info_frame = tk.LabelFrame(settings_frame, text="Project Information", font=("Arial", 12, "bold"))
        info_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        info_text = """
📁 Project Structure:
├── excel_templates/     Excel template files
├── python_scripts/      Python analysis scripts  
├── sample_data/         Sample sales data
├── visualizations/      Generated charts
└── documentation/       User guides

🔧 Features:
• Excel templates with automated formulas
• Data validation and dropdown lists  
• Daily revenue calculations
• Product performance analysis
• Interactive charts and visualizations
• Sample data for testing

📖 Documentation:
Check the documentation/ folder for detailed guides.
        """
        
        tk.Label(
            info_frame,
            text=info_text.strip(),
            justify="left",
            font=("Consolas", 9),
            bg="#f8f9fa"
        ).pack(fill="both", expand=True, padx=10, pady=10)
    
    def create_status_bar(self):
        """Create the status bar at the bottom."""
        status_frame = tk.Frame(self.root, bg="#34495e", height=30)
        status_frame.pack(fill="x", side="bottom")
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            bg="#34495e",
            fg="white",
            font=("Arial", 9)
        )
        self.status_label.pack(side="left", padx=10, pady=5)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            status_frame,
            variable=self.progress_var,
            mode='determinate',
            length=200
        )
        self.progress_bar.pack(side="right", padx=10, pady=5)
        
        self.status_var.set("Ready")
    
    def update_status(self, message):
        """Update the status bar message."""
        self.status_var.set(message)
        self.root.update()
    
    def run_script_async(self, script_path, callback=None):
        """Run a Python script asynchronously."""
        def run():
            try:
                self.update_status(f"Running {os.path.basename(script_path)}...")
                self.progress_var.set(50)
                
                # Get the Python executable path
                python_exe = sys.executable
                if os.path.exists(".venv/bin/python"):
                    python_exe = ".venv/bin/python"
                elif os.path.exists(".venv/Scripts/python.exe"):
                    python_exe = ".venv/Scripts/python.exe"
                
                result = subprocess.run(
                    [python_exe, script_path],
                    capture_output=True,
                    text=True,
                    cwd=os.getcwd()
                )
                
                self.progress_var.set(100)
                
                if result.returncode == 0:
                    self.update_status(f"✅ {os.path.basename(script_path)} completed successfully")
                    if callback:
                        callback(result.stdout)
                else:
                    self.update_status(f"❌ {os.path.basename(script_path)} failed")
                    messagebox.showerror("Error", f"Script failed:\n{result.stderr}")
                
            except Exception as e:
                self.update_status(f"❌ Error running script")
                messagebox.showerror("Error", f"Failed to run script:\n{str(e)}")
            finally:
                self.progress_var.set(0)
        
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()
    
    def create_template(self):
        """Create Excel template."""
        self.run_script_async(
            "python_scripts/create_excel_template.py",
            lambda output: self.refresh_status()
        )
    
    def generate_sample_data(self):
        """Generate sample data."""
        self.run_script_async(
            "python_scripts/generate_sample_data.py",
            lambda output: self.refresh_status()
        )
    
    def generate_custom_data(self):
        """Generate custom sample data with specified days."""
        try:
            days = int(self.days_var.get())
            if days <= 0 or days > 365:
                messagebox.showerror("Error", "Please enter a valid number of days (1-365)")
                return
            
            # Modify the script to accept days parameter
            script_content = f"""
import sys
sys.path.append('python_scripts')
from generate_sample_data import SampleDataGenerator

generator = SampleDataGenerator()
filepath = generator.generate_and_save(days={days})
print(f"Generated {{days}} days of sample data: {{filepath}}")
"""
            
            # Write temporary script
            with open("temp_generate.py", "w") as f:
                f.write(script_content)
            
            self.run_script_async(
                "temp_generate.py",
                lambda output: [self.refresh_status(), os.remove("temp_generate.py") if os.path.exists("temp_generate.py") else None]
            )
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of days")
    
    def run_analysis(self):
        """Run sales analysis."""
        def analysis_callback(output):
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, output)
            self.refresh_charts_list()
            self.refresh_status()
        
        self.run_script_async(
            "python_scripts/sales_analyzer.py",
            analysis_callback
        )
    
    def complete_setup(self):
        """Run complete setup."""
        def setup_callback(output):
            self.refresh_status()
            self.refresh_charts_list()
            messagebox.showinfo("Setup Complete", "All components have been created successfully!")
        
        # Run all scripts in sequence
        def run_sequence():
            scripts = [
                "python_scripts/create_excel_template.py",
                "python_scripts/generate_sample_data.py",
                "python_scripts/sales_analyzer.py"
            ]
            
            for script in scripts:
                if os.path.exists(script):
                    self.run_script_async(script)
        
        run_sequence()
    
    def open_template(self):
        """Open Excel template."""
        template_path = "excel_templates/daily_sales_sheet.xlsx"
        if os.path.exists(template_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(template_path)
                elif sys.platform.startswith('darwin'):
                    subprocess.run(['open', template_path])
                else:
                    subprocess.run(['xdg-open', template_path])
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
        else:
            messagebox.showwarning("File Not Found", "Excel template not found. Please create it first.")
    
    def view_sample_data(self):
        """View sample data file."""
        data_path = "sample_data/sample_sales_data.xlsx"
        if os.path.exists(data_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(data_path)
                elif sys.platform.startswith('darwin'):
                    subprocess.run(['open', data_path])
                else:
                    subprocess.run(['xdg-open', data_path])
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
        else:
            messagebox.showwarning("File Not Found", "Sample data not found. Please generate it first.")
    
    def import_data(self):
        """Import external Excel data."""
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        
        if file_path:
            # Copy file to sample_data directory
            import shutil
            try:
                os.makedirs("sample_data", exist_ok=True)
                dest_path = "sample_data/imported_sales_data.xlsx"
                shutil.copy2(file_path, dest_path)
                messagebox.showinfo("Import Success", f"Data imported successfully to:\n{dest_path}")
                self.refresh_status()
            except Exception as e:
                messagebox.showerror("Import Error", f"Failed to import data:\n{str(e)}")
    
    def view_charts(self):
        """Open visualizations folder."""
        viz_path = "visualizations"
        if os.path.exists(viz_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(viz_path)
                elif sys.platform.startswith('darwin'):
                    subprocess.run(['open', viz_path])
                else:
                    subprocess.run(['xdg-open', viz_path])
            except Exception as e:
                messagebox.showerror("Error", f"Could not open folder:\n{str(e)}")
        else:
            messagebox.showwarning("Folder Not Found", "Visualizations folder not found. Please run analysis first.")
    
    def open_chart(self, event):
        """Open selected chart."""
        selection = self.charts_listbox.curselection()
        if selection:
            chart_name = self.charts_listbox.get(selection[0])
            chart_path = os.path.join("visualizations", chart_name)
            
            if os.path.exists(chart_path):
                try:
                    if sys.platform.startswith('win'):
                        os.startfile(chart_path)
                    elif sys.platform.startswith('darwin'):
                        subprocess.run(['open', chart_path])
                    else:
                        subprocess.run(['xdg-open', chart_path])
                except Exception as e:
                    messagebox.showerror("Error", f"Could not open chart:\n{str(e)}")
    
    def refresh_charts_list(self):
        """Refresh the list of generated charts."""
        self.charts_listbox.delete(0, tk.END)
        
        viz_path = "visualizations"
        if os.path.exists(viz_path):
            charts = [f for f in os.listdir(viz_path) if f.endswith(('.png', '.jpg', '.jpeg', '.txt'))]
            for chart in sorted(charts):
                self.charts_listbox.insert(tk.END, chart)
    
    def refresh_status(self):
        """Refresh project status display."""
        status_text = "PROJECT STATUS\n" + "="*50 + "\n\n"
        
        # Check file existence
        files_to_check = [
            ("Excel Template", "excel_templates/daily_sales_sheet.xlsx"),
            ("Sample Data", "sample_data/sample_sales_data.xlsx"),
            ("Daily Sales Chart", "visualizations/daily_sales_trend.png"),
            ("Product Performance", "visualizations/product_performance.png"),
            ("Category Distribution", "visualizations/category_distribution.png"),
            ("Payment Methods", "visualizations/payment_methods.png"),
            ("Analysis Report", "visualizations/sales_analysis_report.txt")
        ]
        
        for name, path in files_to_check:
            if os.path.exists(path):
                status_text += f"✅ {name}: {path}\n"
            else:
                status_text += f"❌ {name}: Not created yet\n"
        
        # Add summary stats if sample data exists
        sample_path = "sample_data/sample_sales_data.xlsx"
        if os.path.exists(sample_path):
            try:
                import pandas as pd
                df = pd.read_excel(sample_path, sheet_name="Sales Entry")
                total_sales = df['Total Amount'].sum()
                total_transactions = len(df)
                date_range = f"{df['Date'].min()} to {df['Date'].max()}"
                
                status_text += f"\n📊 DATA SUMMARY:\n"
                status_text += f"Period: {date_range}\n"
                status_text += f"Total Transactions: {total_transactions:,}\n"
                status_text += f"Total Sales: ${total_sales:,.2f}\n"
                status_text += f"Average Transaction: ${total_sales/total_transactions:.2f}\n"
                
            except Exception:
                status_text += "\n⚠️ Could not read sample data statistics\n"
        
        status_text += f"\nLast Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, status_text)
    
    def check_dependencies(self):
        """Check if required packages are installed."""
        required_packages = ['pandas', 'openpyxl', 'matplotlib', 'seaborn', 'numpy']
        
        deps_status = "DEPENDENCY CHECK\n" + "="*40 + "\n\n"
        
        for package in required_packages:
            try:
                __import__(package)
                deps_status += f"✅ {package}: Installed\n"
            except ImportError:
                deps_status += f"❌ {package}: Missing\n"
        
        deps_status += f"\n🐍 Python Version: {sys.version}\n"
        deps_status += f"📁 Working Directory: {os.getcwd()}\n"
        deps_status += f"⏰ Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        if hasattr(self, 'deps_text'):
            self.deps_text.delete(1.0, tk.END)
            self.deps_text.insert(tk.END, deps_status)


def main():
    """Main function to start the GUI application."""
    root = tk.Tk()
    app = SalesSheetGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()
