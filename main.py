import csv
import pandas as pd
import glob

def csv_test():
    csv_files = glob.glob('data/*.csv')
    with open('data/daily_sales_data_combined.csv', mode='w') as comb_csv_file:
        fieldnames2 = ['Product', 'Sales', 'Region']
        csv_writer = csv.DictWriter(comb_csv_file, fieldnames2, delimiter=',')
        csv_writer.writeheader()
        for csv_file in csv_files:
            if csv_file == 'data/daily_sales_data_combined.csv':
                continue
            fieldnames1 = ['Product_Name', 'Price', 'Quantity', 'Date', 'Region']
            with open(csv_file) as file:
                csv_reader = csv.DictReader(file, fieldnames1, delimiter=',')
                for row in csv_reader:
                    if row['Product_Name'] == 'pink morsel':
                        sale = '$' + str(float((row['Price'])[1:]) * float(row['Quantity']))
                        csv_writer.writerow({'Product': row['Product_Name'], 'Sales': sale, 'Region': row['Region']})

#Above is the CSV example

# def panda_test():
#     df = pd.read_csv('data/daily_sales_data_0.csv', index_col = 'Product_Name', parse_dates = ['Date'], header = 0, names = ['Product_Name', 'Price', 'Quantity', 'Date', 'Region'])
#     # print(type(df['date']))
#     # Used to check the type of data for the index column.
#     filteredDf = df[df['Product_Name'] == 'pink morsel']
#     for row in filteredDf:
#         print(row)
#         if(row[0] == 'pink morsel'):
#             print(row)
#             break
    #df is short for DataFrame, which is a pandas data structure that stores data in rows and columns
# panda_test()

csv_test()
# Based on current experience(less than 1 hour)
#   pandas may be easier to read in a table, more structured,
#   compared to the csv files, but csv files is easier to manipulate, simple data