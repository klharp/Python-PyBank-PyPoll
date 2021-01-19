# Financial Analysis
# ---------------------

import os
import csv

# Lists to store data
id = []
candidates = []

#Define variables
total_votes = 0

# Open provided csv
csvpath = os.path.join('Resources', 'election_data.csv')

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

        # Put id in list
        id.append(row[0])
        # print(id)

        # Put candidates in list
        candidates.append(row[2])
        # print(candidates)
        
# Get total number of votes
total_votes = len(id)
# print(total_votes)

# Get unique candidates
candidate_name = list(set(candidates))
print(candidate_name)