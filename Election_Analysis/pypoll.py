
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
csv_elec_results = 'resources/election_results.csv'

#open the election results and read the file
#CODE:election_data = open(csv_elec_results, 'r')
        
        #Alternative open/close process
with open(csv_elec_results) as election_data:


#add analysis code at later date

#close the file
#election_data.close()
        #Alternative close process
    print(election_data)
