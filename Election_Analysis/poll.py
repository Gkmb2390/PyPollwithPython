# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Accumulators i.e. counters
#1) Total Vote Counter
total_votes = 0
#declare empty candidate list 
candidate_options = []
#declare empty candidate dictionary 
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    ##print(headers)
    
    #Print Each Row in the CSV File
    for row in file_reader:
        #print(row)
        #2 Add to Total Vote Count 
        total_votes += 1
        #print the candidate names from each row
        candidate_name = row[2]  
        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        # add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin Tracking Candidate vote count
            candidate_votes[candidate_name] = 0

        #increase candidate votes by 1
        candidate_votes[candidate_name] +=1
for candidate_name in candidate_votes:
    # Retrieve vot count of the candidate
    votes=candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage =float(votes)/ float(total_votes)*100
    #print candidate name and vote percentage
    print(f'{candidate_name}: recieved {vote_percentage:.1f}% of the vote')
#3 Print Total Votes
#print(total_votes)
#4 print candidate list
#print(candidate_options)
#5 print candidate vote dictionary
print(candidate_votes)
#6 print the candidate vote percentage
print