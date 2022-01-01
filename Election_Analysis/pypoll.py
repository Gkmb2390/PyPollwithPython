
## What our code needs to do
    #1. Total Number of votes cast
    #2. A complete list of candidates recieved
    #3. Total number of votes per candidate
    #4. percentage of votes per candidate
    #5. winner of election based on Popular Vote

### Variables from CSV in column order
    #1 ID
    #2 County
    #3 Candidate

# pseudocode
    #Open File
    #Write down the names of all the candidates
    #add a vote count for each Candidate
    #Get total votes cast for the election

#Assign variable for loading the file
    # Direct Path technique - csv_elec_results = 'resources\election_results.csv'

    #Indirect Path Technique
import csv
import os
#csv_elec_results = os.path.join("analysis","election_results.txt")
#open(csv_elec_results, "w")
#open the election results and read the file
#CODE:election_data = open(csv_elec_results, 'r')
        
        #Alternative open/close process
#with open(csv_elec_results) as election_data:
    #add analysis code at later date

#close the file
#election_data.close()
        #Alternative close process
 #   print(election_data)

## Writing from python to file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
    #writing single items to document
#outfile.write("Arapahoe, ")
#outfile.write("Denver, ")
#outfile.write("Jefferson, ")

    #writing multiple items to a document
#outfile.write("Araphoe, Denver, Jefferson")

    ##Writing with NEW LINE ESCAPE SEQUENCE
outfile.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJeffeson")

# Close the file
outfile.close()