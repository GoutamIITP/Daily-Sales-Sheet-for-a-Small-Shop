"""
Sales Data Analysis and Visualization
Analyzes sales data from Excel files and generates insights and charts.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os


class SalesAnalyzer:
    """Analyzes sales data and creates visualizations."""
    
    def __init__(self, excel_file_path: str):
        """Initialize the analyzer with Excel file path."""
        self.excel_file = excel_file_path
        self.sales_data = None
        self.output_dir = "visualizations"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_sales_data(self) -> pd.DataFrame:
        """Load sales data from Excel file."""
        try:
            self.sales_data = pd.read_excel(self.excel_file, sheet_name="Sales Entry")
            
            # Clean and prepare data
            self.sales_data['Date'] = pd.to_datetime(self.sales_data['Date'])
            self.sales_data = self.sales_data.dropna(subset=['Product Name', 'Date'])
            
            # Ensure numeric columns
            numeric_columns = ['Quantity Sold', 'Unit Price', 'Total Amount']
            for col in numeric_columns:
                self.sales_data[col] = pd.to_numeric(self.sales_data[col], errors='coerce')
            
            print(f"Loaded {len(self.sales_data)} sales records")
            return self.sales_data
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
    
    def calculate_daily_summary(self) -> pd.DataFrame:
        """Calculate daily sales summary."""
        if self.sales_data is None or self.sales_data.empty:
            return pd.DataFrame()
        
        daily_summary = self.sales_data.groupby('Date').agg({
            'Total Amount': ['sum', 'count', 'mean'],
            'Quantity Sold': 'sum',
            'Product Name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'N/A'
        }).round(2)
        
        # Flatten column names
        daily_summary.columns = ['Total Sales', 'Total Transactions', 'Average Sale', 'Total Quantity', 'Best Selling Product']
        daily_summary = daily_summary.reset_index()
        
        return daily_summary
    
    def analyze_product_performance(self) -> pd.DataFrame:
        """Analyze product performance metrics."""
        if self.sales_data is None or self.sales_data.empty:
            return pd.DataFrame()
        
        product_analysis = self.sales_data.groupby('Product Name').agg({
            'Quantity Sold': 'sum',
            'Total Amount': ['sum', 'mean'],
            'Date': ['min', 'max', 'count']
        }).round(2)
        
        # Flatten column names
        product_analysis.columns = ['Total Quantity', 'Total Revenue', 'Avg Sale Value', 'First Sale', 'Last Sale', 'Sale Count']
        product_analysis = product_analysis.reset_index()
        product_analysis = product_analysis.sort_values('Total Revenue', ascending=False)
        
        return product_analysis
    
    def create_daily_sales_chart(self) -> str:
        """Create daily sales trend chart."""
        daily_summary = self.calculate_daily_summary()
        
        if daily_summary.empty:
            return "No data available for chart"
        
        plt.figure(figsize=(12, 6))
        plt.plot(daily_summary['Date'], daily_summary['Total Sales'], marker='o', linewidth=2, markersize=6)
        plt.title('Daily Sales Trend', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        chart_path = os.path.join(self.output_dir, 'daily_sales_trend.png')
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return chart_path
    
    def create_product_performance_chart(self) -> str:
        """Create product performance bar chart."""
        product_data = self.analyze_product_performance()
        
        if product_data.empty:
            return "No data available for chart"
        
        # Top 10 products by revenue
        top_products = product_data.head(10)
        
        plt.figure(figsize=(12, 8))
        bars = plt.bar(range(len(top_products)), top_products['Total Revenue'])
        plt.title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
        plt.xlabel('Products', fontsize=12)
        plt.ylabel('Total Revenue ($)', fontsize=12)
        plt.xticks(range(len(top_products)), top_products['Product Name'].tolist(), rotation=45, ha='right')
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'${height:.0f}', ha='center', va='bottom')
        
        plt.tight_layout()
        
        chart_path = os.path.join(self.output_dir, 'product_performance.png')
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return chart_path
    
    def create_category_analysis_chart(self) -> str:
        """Create category sales distribution chart."""
        if self.sales_data is None or self.sales_data.empty:
            return "No data available for chart"
        
        category_sales = self.sales_data.groupby('Category')['Total Amount'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(10, 8))
        colors = plt.get_cmap('Set3')(np.linspace(0, 1, len(category_sales))).tolist()
        pie_result = plt.pie(category_sales.to_numpy(), labels=category_sales.index.tolist(), 
                             autopct='%1.1f%%', colors=colors, startangle=90)
        if len(pie_result) == 3:
            wedges, texts, autotexts = pie_result
        else:
            wedges, texts = pie_result
            autotexts = []
        
        plt.title('Sales Distribution by Category', fontsize=16, fontweight='bold')
        
        # Enhance text appearance
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        chart_path = os.path.join(self.output_dir, 'category_distribution.png')
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return chart_path
    
    def create_payment_method_chart(self) -> str:
        """Create payment method distribution chart."""
        if self.sales_data is None or self.sales_data.empty:
            return "No data available for chart"
        
        payment_data = self.sales_data.groupby('Payment Method').agg({
            'Total Amount': 'sum',
            'Date': 'count'
        }).round(2)
        payment_data.columns = ['Total Amount', 'Transaction Count']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Revenue by payment method
        payment_data['Total Amount'].plot(kind='bar', ax=ax1, color='skyblue')
        ax1.set_title('Revenue by Payment Method', fontweight='bold')
        ax1.set_ylabel('Total Revenue ($)')
        ax1.tick_params(axis='x', rotation=45)
        
        # Transaction count by payment method
        payment_data['Transaction Count'].plot(kind='bar', ax=ax2, color='lightcoral')
        ax2.set_title('Transaction Count by Payment Method', fontweight='bold')
        ax2.set_ylabel('Number of Transactions')
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        chart_path = os.path.join(self.output_dir, 'payment_methods.png')
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return chart_path
    
    def generate_sales_report(self) -> str:
        """Generate comprehensive sales report."""
        if self.sales_data is None:
            self.load_sales_data()
        
        if self.sales_data.empty:
            return "No data available for analysis"
        
        # Calculate key metrics
        total_revenue = self.sales_data['Total Amount'].sum()
        total_transactions = len(self.sales_data)
        avg_transaction = self.sales_data['Total Amount'].mean()
        best_selling_product = self.sales_data.groupby('Product Name')['Quantity Sold'].sum().idxmax()
        date_range = f"{self.sales_data['Date'].min().date()} to {self.sales_data['Date'].max().date()}"
        
        # Generate charts
        daily_chart = self.create_daily_sales_chart()
        product_chart = self.create_product_performance_chart()
        category_chart = self.create_category_analysis_chart()
        payment_chart = self.create_payment_method_chart()
        
        # Create report
        report = f"""
DAILY SALES ANALYSIS REPORT
==========================

Period: {date_range}

KEY METRICS:
-----------
Total Revenue: ${total_revenue:,.2f}
Total Transactions: {total_transactions:,}
Average Transaction Value: ${avg_transaction:.2f}
Best Selling Product: {best_selling_product}

GENERATED VISUALIZATIONS:
------------------------
1. Daily Sales Trend: {daily_chart}
2. Product Performance: {product_chart}
3. Category Distribution: {category_chart}
4. Payment Methods: {payment_chart}

INSIGHTS:
---------
- Peak sales days and trends
- Top performing products and categories
- Customer payment preferences
- Revenue distribution patterns

All charts have been saved to the 'visualizations' folder.
        """
        
        # Save report to file
        report_path = os.path.join(self.output_dir, 'sales_analysis_report.txt')
        with open(report_path, 'w') as f:
            f.write(report)
        
        return report


def main():
    """Main function to run sales analysis."""
    # First try to use sample data, then template
    excel_file = "sample_data/sample_sales_data.xlsx"
    
    if not os.path.exists(excel_file):
        excel_file = "excel_templates/daily_sales_sheet.xlsx"
        if not os.path.exists(excel_file):
            print(f"No data file found. Please run:")
            print("1. create_excel_template.py to create the template")
            print("2. generate_sample_data.py to create sample data")
            return
    
    print("Starting Sales Data Analysis...")
    analyzer = SalesAnalyzer(excel_file)
    
    # Load data and generate report
    analyzer.load_sales_data()
    report = analyzer.generate_sales_report()
    
    print(report)
    print(f"\nAnalysis complete! Check the 'visualizations' folder for charts and reports.")


if __name__ == "__main__":
    main()
