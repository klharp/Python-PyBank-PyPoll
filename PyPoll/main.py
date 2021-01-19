'''
I started this using empty lists to store id and candidate data, thinking I could loop
through the data to get the info needed. Switched to putting the data into a dictionary 
with the candidate as key and the vote count as the value. 
Sought help with the dictionary part (Thanks TA Farshad!).

'''
# Elections Results
# --------------------- 

import os
import csv

# Lists to store data
id = []


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

        # Add candidate vote counts to dictionary value
            # candidates (row[2]) is the key(s) added to empty candidate_dict
            # vote_count is the value(s)
        #counts the first item list as a vote
        vote_count += 1 #vote_count = vote_count +1
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
        else:
            candidate_dict[row[2]] += 1
        # print(candidate_dict)
              
# Get total number of votes
total_votes = len(id)
# print(total_votes)

# Create empty lists for name and vote data from dictionary
summary_candidate = []
summary_votes = []
winner = []

# Add key and value to empty lists
for key, value in candidate_dict.items():
    summary_candidate.append(key)
    # print(summary_candidate)

    # for key, value in candidate_dict.items():
    summary_votes.append(value)
    # print(summary_votes)

# Find the winner
winner = max(candidate_dict, key=candidate_dict.get)
# print(winner)   

# Prepare summary
print("Election Results")
print("-------------------------------------")
print(summary_candidate[0] + " " + "{:.3%}".format(summary_votes[0]/total_votes) + " (" + str(summary_votes[0]) + ")")
print(summary_candidate[1] + " " + "{:.3%}".format(summary_votes[1]/total_votes) + " (" + str(summary_votes[1]) + ")")
print(summary_candidate[2] + " " + "{:.3%}".format(summary_votes[2]/total_votes) + " (" + str(summary_votes[2]) + ")")
print(summary_candidate[3] + " " + "{:.3%}".format(summary_votes[3]/total_votes) + " (" + str(summary_votes[3]) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# # Export to text file
output_text = os.path.join("analysis", "ElectionResults.txt")
with open(output_text, "w") as textfile:
    textfile.write("Election Results" "\n")
    textfile.write("-------------------------------------""\n")
    textfile.write(summary_candidate[0] + " " + "{:.3%}".format(summary_votes[0]/total_votes) + " (" + str(summary_votes[0]) + ")"  "\n")
    textfile.write(summary_candidate[1] + " " + "{:.3%}".format(summary_votes[1]/total_votes) + " (" + str(summary_votes[1]) + ")"  "\n")
    textfile.write(summary_candidate[2] + " " + "{:.3%}".format(summary_votes[2]/total_votes) + " (" + str(summary_votes[2]) + ")"  "\n")
    textfile.write(summary_candidate[3] + " " + "{:.3%}".format(summary_votes[3]/total_votes) + " (" + str(summary_votes[3]) + ")"  "\n")
    textfile.write("-------------------------------------""\n")
    textfile.write("Winner: " + winner + "\n")
    textfile.write("-------------------------------------")