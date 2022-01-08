# PyPollwithPython
Module 3 Challenge

# Overview of Project
Analyze the election data in order to determine the winner of the election.  Additionally we want to acknoledge the number of votes & percentages of votes cast for the other candidates, as well as the number of votes and percentages cast by each county.  Specifically we are looking to acknowedge the largest county by voter turnout. 

# Election Audit Results:
## Total Votes Cast
1. The number of total votes cast in the election was 369,711.  This was determined by counting the total number of rows in both the Candidate and County rows; in 2 seperate sections of the code (image below)
        
        [Total Votes Code Image](https://github.com/Gkmb2390/PyPollwithPython/blob/main/Election_Analysis/Resources/County%20Vote%20Highlight.png)

These sections of code allow for us to count the total votes by adding 1 value to the total_votes for the rows being counted for in the loop, specifcally the candidate names and the county names.
## Breakdown of Election by County
2. See the image below for the breakdown of each county with the vote count and percentage that was determined from the csv & code.
        
        [County Results from Txt File](https://github.com/Gkmb2390/PyPollwithPython/blob/main/Election_Analysis/Resources/Vote%20Total%20Count%20Code.png)
## Largest County Results    
3. The largest county was determined to be Denver county.  As seen in the image above, Denver county has an overwhelming majority of voter turnout at over 270 votes totaled and nearly 75% of the total votes for the election
## Candidate Results
4. The candidates recieved the following vote counts and percentages:
        Charles Casper Stockham: 23.0%  (85,213)
        Diana DeGette: 73.8%  (272,892)
        Raymon Anthony Doane: 3.1%  (11,606)
## Election Winner
5. Diana Degette won the election my a landslide securing 73.8% of the votes in the election which eqates to 272,892 votes.  Her nearest rival was Charles Stockham at only 23% which equates to roughly 85K votes. 

# Election Audit Summary
    After reviewing the results of our script for the election, I firmly believe that this script can and should be used to account for future elections.  Not only did we determine the winning candidate to the precise vote, but we did it with minimal effort and very efficiently. 

    In consideration of future elections we may consider the following changes to code:
1. We could include a for loop that reviews each ballot ID and introduces the ID's to a dictionary or list.
Adding the following code before the loops most likely with the other declared dictironaries(see image below) would establish a voter ID dictionary
    [Dictionary Images from code](https://github.com/Gkmb2390/PyPollwithPython/blob/main/Election_Analysis/Resources/Dictionaries%20setup%20image.png)
    voter_ID_dict = {}

2. We would then be able to confirm that no 1 voter ID is being accounted for multiple times within the script.  
    [first for loop code image](https://github.com/Gkmb2390/PyPollwithPython/blob/main/Election_Analysis/Resources/first%20for%20loop%20image.png)
    
    Adding the below code in the first for loop.
    Voter_ID = row[0]
    
    if Voter_ID not in voter_ID_dict:

            # Add the candidate name to the candidate list.
            voter_ID_dict.append(Voter_ID)
    
    Using our Voter ID Dictionary as a source we should be able to confirm if there are any duplicate values for voter ID. 


