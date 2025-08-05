#!/usr/bin/env python3
"""
GUI Launcher for Daily Sales Sheet Management System
Direct launcher for the tkinter GUI application.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Launch the GUI application directly."""
    try:
        import tkinter as tk
        print("🏪 Starting Daily Sales Sheet GUI...")
        
        # Import and run the GUI
        from gui_app import SalesSheetGUI
        
        root = tk.Tk()
        app = SalesSheetGUI(root)
        
        # Center the window
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")
        
        print("✅ GUI application started successfully!")
        root.mainloop()
        
    except ImportError as e:
        print("❌ Error: GUI dependencies not available.")
        print(f"Missing: {e}")
        print("\nPlease ensure tkinter is installed with your Python distribution.")
        print("On Ubuntu/Debian: sudo apt-get install python3-tk")
        print("On CentOS/RHEL: sudo yum install tkinter")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        print("\nFalling back to command-line interface...")
        
        # Fallback to CLI
        try:
            from main import main as cli_main
            cli_main()
        except Exception as cli_error:
            print(f"❌ CLI also failed: {cli_error}")
            sys.exit(1)


if __name__ == "__main__":
    main()
