import re
import csv
from collections import Counter
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)

# Daily sales data
daily_sales = """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17"""

# Clean and split the data (updated regular expression for splitting)
daily_sales_cleaned = re.split(r'\s*,\s*|\s*;\,;\s*|\s*\n\s*', daily_sales.strip())
transactions = [daily_sales_cleaned[i:i+4] for i in range(0, len(daily_sales_cleaned), 4)]

# Function to validate and parse data
def parse_data(transaction):
    """Validates and parses each transaction"""
    if len(transaction) != 4:
        logging.error(f"Malformed transaction: {transaction}")
        return None
    customer, sale, thread, _ = transaction
    try:
        sale_amount = float(sale.strip('$'))
    except ValueError:
        logging.error(f"Invalid sale value: {sale}")
        return None
    if not all(color in ['white', 'blue', 'green', 'yellow', 'red', 'purple', 'black'] for color in thread.split('&')):
        logging.error(f"Invalid thread color: {thread}")
        return None
    return customer, sale_amount, thread

# Filter and process valid transactions
valid_transactions = filter(None, (parse_data(transaction) for transaction in transactions))

# Extract data
try:
    customers, sales, thread_sold = zip(*valid_transactions)
except ValueError:
    logging.error("No valid transactions to process.")
    customers, sales, thread_sold = [], [], []

# Calculate total sales
total_sales = sum(sales)
print(f"Total Sales: ${total_sales:.2f}")

# Count thread colors sold
color_counts = Counter(color for thread in thread_sold for color in thread.split('&'))
available_colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
for color in available_colors:
    print(f"Today, {color_counts.get(color, 0)} threads of color {color} were sold.")

# Save data to CSV
def save_sales_to_csv(customers, sales, thread_sold, filename="sales_report.csv"):
    """Saves the transactions to a CSV file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Customer", "Sale Amount", "Thread Sold"])
        writer.writerows(zip(customers, sales, thread_sold))
    print(f"Data saved to {filename}")

# Save the transactions to a CSV file
save_sales_to_csv(customers, sales, thread_sold)
