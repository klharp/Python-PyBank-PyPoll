# Financial Analysis
# ---------------------

import os
import csv

# Lists to store data
dates = []
revenue = [] #profit or loss
monthly_revenue_change = []

#Define variables
total_revenue = 0
max_increase_revenue = 0
min_increase_revenue = 0

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

# Find the max values for increase and then decrease in profits
max_increase_revenue = max(monthly_revenue_change)
min_increase_revenue = min(monthly_revenue_change)
# print(max_increase_revenue)
# print(min_increase_revenue)

# Find the dates of the increase and decrease 
max_month = dates[monthly_revenue_change.index(max_increase_revenue)+1]
min_month = dates[monthly_revenue_change.index(min_increase_revenue)+1]
# print(max_month)
# print(min_month)

# Prepare summary
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total_revenue))
print("Average Change: " + str(round(average_revenue_change,2)))
print("Greatest Increase in Profits: " + str(max_month) + " " + "($" + str(max_increase_revenue) + ")")
print("Greates Decrease in Profits: " + str(min_month) + " " + "($" + str(min_increase_revenue) + ")")

# Export to text file
output_text = os.path.join("analysis", "FinancialAnalysis.txt")
with open(output_text, "w") as textfile:
    textfile.write("Financial Analysis" "\n")
    textfile.write("-------------------------------------""\n")
    textfile.write("Total Months: " + str(months) + "\n")
    textfile.write("Total: $" + str(total_revenue) + "\n")
    textfile.write("Average Change: " + str(round(average_revenue_change,2)) +"\n")
    textfile.write("Greatest Increase in Profits: " + str(max_month) + " " + "($" + str(max_increase_revenue) + ")""\n")
    textfile.write("Greates Decrease in Profits: " + str(min_month) + " " + "($" + str(min_increase_revenue) + ")""\n")