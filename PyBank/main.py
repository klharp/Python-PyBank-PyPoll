# financial analysis
# ---------------------

import os
import csv

# Lists to store data
dates = []
revenue = [] #profit or loss
monthly_revenue_change = []
monthly_date_change = []


#Define variables
total_revenue = 0
max_increase_revenue = 0
min_decrease_revenue = 0
prev_month_revenue = 0


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
        revenue.append(int(row[1]))
        # sprint(revenue)
        
# Find total revenue
total_revenue = sum(revenue)
# print(total_revenue)

# Get total number of months
months = 0
months = len(dates)
# print(months)

# Create list to hold values for revenue changes
monthly_revenue_change = [revenue[i + 1] - revenue[i] for i in range(0,len(revenue)-1)]
# print(monthly_revenue_change)

# Find the average value for revenue changes
average_revenue_change = (sum(monthly_revenue_change) / len(monthly_revenue_change))
# print(average_revenue_change)

# Loop to get the max values for increase and then decrease in profits
for i in range(len(monthly_revenue_change)-1):
    if monthly_revenue_change[i] > max_increase_revenue:
        max_increase_revenue = monthly_revenue_change[i]

    if monthly_revenue_change[i] < min_decrease_revenue:
        min_decrease_revenue = monthly_revenue_change[i]

print(max_increase_revenue)       
print(min_decrease_revenue)

# Get the min values for decrease in profits

