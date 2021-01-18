# financial analysis
# ---------------------

import os
import csv

# Empty lists to store data
dates = []
revenue = [] #profit or loss
monthly_revenue_change = []
monthly_date_change = []


#Define variables
total_revenue = 0
prev_revenue = 0
inc_revenue = 0
dec_revenue = 0


# Open provided csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read the csv and remove header
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

 
    # Loop through each row of data after the header to get values
    for row in csvreader:

        # Put dates in list
        dates.append(row[0])
        # print(dates)

        # Put monthly profit & loss values (revenue) in list
        revenue.append(row[1])
        # print(revenue)

        # Total the profit & loss values in the column
        total_revenue += float(row[1])
        # print(total_revenue)

        # Find the monthly change in revenue
        monthly_revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        monthly_date_change = monthly_date_change + [row[0]]
        print(monthly_revenue_change)
        # print(monthly_date_change)


# Get total number of months
months = len(dates)
# print(months)

