# Elections Analysis
# ---------------------

import os
import csv

# Lists to store data
id = []
candidates = []

# Dictionary to store incremental votes
candidate_dict = {}

# Define variables
total_votes = 0
vote_count = 1

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

        # Add candidate vote counts to dictionary value
            # candidates is the key added to empty candidate_dict
            # vote_count is the value(s)
        #counts the first item list as a vote
        vote_count += 1 #vote_count = vote_count +1
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
        else:
            candidate_dict[row[2]] += 1
        candidate_dict["Kahn"] = 1   
        # print(candidate_dict)
              
# Get total number of votes
total_votes = len(id)
# print(total_votes)

# Get unique candidates and put in list
candidate_name = list(set(candidates))
# print(candidate_name)

 # need to determine votes per candidate
    # Is this done in a for loop? 
    # Would a dictionary work better? Can put the list of the 4 candidates and return the 4 names as values?
        #If using a dictionary, how do I loop row by row to tally the votes per candidate?

#Use the info above to determine who won based on the most votes.    

#Create Summary Table

#Export Summary Table