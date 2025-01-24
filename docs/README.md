# sales-data-organizer

This project demonstrates how to clean and organize transaction data using Python. The initial data is stored in a messy string format, with various delimiters and inconsistent entries. The goal is to parse the string, split it into individual transactions, and cleanly organize the information into structured lists for easier analysis.

## Exercise: Parsing and Organizing Sales Data

Key steps in this exercise include:

- Replacing delimiters and splitting the string into individual transaction entries.
- Splitting each transaction into customer names, sales amounts, and thread colors sold.
- Calculating total sales and counting the occurrences of different thread colors sold.
- Using Python's list comprehensions and built-in functions to efficiently process and clean the data.

The final output includes:

- A list of customers, sales, and threads sold.
- A total sales amount.
- A breakdown of thread sales by color.

This exercise provides hands-on experience with list manipulation, string processing, and basic data analysis in Python.

## Example Usage

Run the script to clean and organize the sales data

```bash
$ python transaction_cleaner.py

```

## Example Output

- Total Sales: $185.65
- Today, 2 threads of color white were sold.
- Today, 2 threads of color purple were sold.
- Today, 1 thread of color blue was sold.
...

## File Structure
- transaction_cleaner.py: The main script that processes and cleans the sales data.
- sales_report.csv: The file where the cleaned and organized data is saved.

## License

This project is licensed under the Apache License, Version 2.0. You can obtain a copy of the license at:

[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)