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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    ##print(headers)
    
    #Print Each Row in the CSV File
    for row in file_reader:
       #2 Add to Total Vote Count 
       total_votes += 1
       
       #print(row)
#3 Print Total Votes
print(total_votes)