"""
Sample Sales Data Generator
Generates realistic sample sales data for testing the Daily Sales Sheet system.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os


class SampleDataGenerator:
    """Generates sample sales data for testing purposes."""
    
    def __init__(self):
        self.products = {
            'Food': ['Sandwich', 'Burger', 'Pizza Slice', 'Salad', 'Wrap', 'Soup'],
            'Beverage': ['Coffee', 'Tea', 'Juice', 'Soda', 'Water', 'Smoothie'],
            'Snack': ['Chips', 'Cookies', 'Nuts', 'Fruit', 'Granola Bar', 'Crackers'],
            'Dessert': ['Cake', 'Ice Cream', 'Pastry', 'Muffin', 'Donut', 'Pie']
        }
        
        self.payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment']
        self.customer_types = ['Regular', 'New', 'VIP', 'Student', 'Senior']
        
        # Price ranges for different categories
        self.price_ranges = {
            'Food': (5.99, 15.99),
            'Beverage': (1.99, 6.99),
            'Snack': (0.99, 4.99),
            'Dessert': (2.99, 8.99)
        }
    
    def generate_sample_data(self, days: int = 30, min_transactions_per_day: int = 20, 
                           max_transactions_per_day: int = 50) -> pd.DataFrame:
        """Generate sample sales data for specified number of days."""
        
        sales_data = []
        start_date = datetime.now() - timedelta(days=days)
        
        for day in range(days):
            current_date = start_date + timedelta(days=day)
            
            # Vary transactions based on day of week (weekends busier)
            if current_date.weekday() in [5, 6]:  # Weekend
                num_transactions = random.randint(int(max_transactions_per_day * 0.8), max_transactions_per_day)
            else:  # Weekday
                num_transactions = random.randint(min_transactions_per_day, int(max_transactions_per_day * 0.7))
            
            for _ in range(num_transactions):
                # Select random category and product
                category = random.choice(list(self.products.keys()))
                product = random.choice(self.products[category])
                
                # Generate realistic quantity (most sales are 1-3 items)
                quantity = random.choices([1, 2, 3, 4, 5], weights=[50, 30, 15, 4, 1])[0]
                
                # Generate price within category range
                min_price, max_price = self.price_ranges[category]
                unit_price = round(random.uniform(min_price, max_price), 2)
                
                # Calculate total
                total_amount = round(quantity * unit_price, 2)
                
                # Select payment method and customer type
                payment_method = random.choice(self.payment_methods)
                customer_type = random.choice(self.customer_types)
                
                # Add some time variation within the day
                hour = random.randint(8, 20)  # Shop open 8 AM to 8 PM
                minute = random.randint(0, 59)
                transaction_time = current_date.replace(hour=hour, minute=minute)
                
                sales_data.append({
                    'Date': transaction_time.date(),
                    'Product Name': product,
                    'Category': category,
                    'Quantity Sold': quantity,
                    'Unit Price': unit_price,
                    'Total Amount': total_amount,
                    'Payment Method': payment_method,
                    'Customer Type': customer_type
                })
        
        return pd.DataFrame(sales_data)
    
    def save_sample_data(self, data: pd.DataFrame, filename: str = "sample_sales_data.xlsx") -> str:
        """Save sample data to Excel file."""
        os.makedirs("sample_data", exist_ok=True)
        filepath = os.path.join("sample_data", filename)
        
        # Create Excel file with multiple sheets
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            # Main sales data
            data.to_excel(writer, sheet_name='Sales Entry', index=False)
            
            # Daily summary
            daily_summary = data.groupby('Date').agg({
                'Total Amount': ['sum', 'count', 'mean'],
                'Quantity Sold': 'sum'
            }).round(2)
            daily_summary.columns = ['Total Sales', 'Total Transactions', 'Average Sale', 'Total Quantity']
            daily_summary.to_excel(writer, sheet_name='Daily Summary')
            
            # Product analysis
            product_summary = data.groupby(['Product Name', 'Category']).agg({
                'Quantity Sold': 'sum',
                'Total Amount': ['sum', 'mean'],
                'Date': 'count'
            }).round(2)
            product_summary.columns = ['Total Quantity', 'Total Revenue', 'Avg Sale Value', 'Sale Count']
            product_summary.to_excel(writer, sheet_name='Product Analysis')
        
        return filepath
    
    def generate_and_save(self, days: int = 30) -> str:
        """Generate and save sample data in one step."""
        print(f"Generating {days} days of sample sales data...")
        
        sample_data = self.generate_sample_data(days)
        filepath = self.save_sample_data(sample_data)
        
        # Print summary statistics
        total_sales = sample_data['Total Amount'].sum()
        total_transactions = len(sample_data)
        avg_transaction = sample_data['Total Amount'].mean()
        date_range = f"{sample_data['Date'].min()} to {sample_data['Date'].max()}"
        
        print(f"\nSample data generated successfully!")
        print(f"File saved: {filepath}")
        print(f"\nData Summary:")
        print(f"- Period: {date_range}")
        print(f"- Total Transactions: {total_transactions:,}")
        print(f"- Total Sales: ${total_sales:,.2f}")
        print(f"- Average Transaction: ${avg_transaction:.2f}")
        print(f"- Products: {sample_data['Product Name'].nunique()} unique items")
        print(f"- Categories: {', '.join(sample_data['Category'].unique())}")
        
        return filepath


def main():
    """Generate sample sales data."""
    generator = SampleDataGenerator()
    
    # Generate 30 days of sample data
    filepath = generator.generate_and_save(days=30)
    
    print(f"\nYou can now:")
    print("1. Open the sample data file to review the generated data")
    print("2. Copy data to your Excel template for testing")
    print("3. Run the sales analyzer to see charts and reports")


if __name__ == "__main__":
    main()
