# Sales Report Consolidator

## About

Managing sales reports from multiple branches or different months can quickly become time-consuming and error-prone. This project automatically combines multiple sales CSV files into a single dataset and generates summary reports showing total quantities sold, average quantities, and the number of sales per product. It helps businesses consolidate sales data in seconds, reducing manual work and improving reporting accuracy.

## Key Features

* **Automatic CSV Merging:** Combines multiple sales CSV files into one consolidated dataset.
* **Sales Summary Generation:** Calculates total quantity sold, average quantity sold, and number of sales for every product.
* **Business Statistics:** Displays useful insights such as highest sale, lowest sale, average sale quantity, and total number of records.
* **Fast Batch Processing:** Processes multiple monthly sales reports automatically.
* **Business-Ready Output:** Exports both the merged dataset and summary report as clean CSV files.
* **Modular Python Design:** Uses reusable functions to make the code easy to understand, maintain, and extend.

## Technologies Used

* Python 3
* Pandas
* Glob
* Pathlib
* CSV Files

## Folder Structure

```text
sales-report-consolidator/
│
├── README.md
├── sales_report_consolidator.py
│
├── sample_data/
│   ├── january.csv
│   ├── february.csv
│   └── march.csv
│
├── output/
│   ├── merged_sales.csv
│   └── sales_summary.csv
│
└── screenshots/
    ├── original-files.png
    ├── merged-report.png
    ├── summary-report.png
    └── terminal-output.png
```

## How to Run

1. Install Python 3.
2. Install Pandas:

```bash
pip install pandas
```

3. Run the program:

```bash
python sales_report_consolidator.py
```

4. The program automatically merges the sales reports and generates:

* `merged_sales.csv`
* `sales_summary.csv`

## Example Output

### Sales Summary

 Product  Total Quantity  Average Quantity  Number of Sales 
 -------  -------------:  ---------------:  --------------: 
 Bread                25             12.50                2 
 Eggs                 60             60.00                1 
 Milk                 50             25.00                2 
 Rice                 25             25.00                1 
 Sugar                40             40.00                1 

## Future Improvements

* Support Excel (.xlsx) sales reports.
* Generate PDF sales reports automatically.
* Allow users to select the input folder from the command line.
* Add charts showing product sales trends.
* Build a simple graphical user interface (GUI).



