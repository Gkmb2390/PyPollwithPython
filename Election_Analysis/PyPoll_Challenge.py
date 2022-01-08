# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
# Create a list based on the counties involved in election
county_options = []
# Create a dictionary based on the votes per county in the election
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# setting up largest county variable as a literal, so that we can backfill once the county with most votes is determined
largest_county = ""
# setting up variable for the largest # of county votes so that we will have a value to key off for largetst county
county_voter_turnout = 0
# setting up a variable for the Winning County vote to be filled once the county with most votes has been determined
winning_county_vote = 0
# setting up a vairable for the winning county percentage to be filled in once we have determined which county had the most votes
winning_county_percentage = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        # after reviewing csv file we see the county name is in the 2nd row of the sheet; which would equate to the 1st position in the file since the starting row is 0. 
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        # setting up a if then statement with the additional conditional of "not in" which will be useful in step 4b
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            # Using the "not in" logic from the above section, we are adding the county_name variable to the county_options list; only if the county_name does not already exist within the list.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            # Using the county_votes dictionary we can establish the number of votes as 0 for each county name of our list.  The varibale listed within the county_votes list allows for the pairs of votes to county names to be created.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        # This reviews each county name in the row and adds 1 value each time the county name is repeated; since we established the county votes list prior to this step, we know that each list is beginning at 0
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    #beginning the 'for' loop looking for the county names in the county_options list 
    for county_name in county_options:
        # 6b: Retrieve the county vote count.
        # The County_vote_count variable is equal to the value of the County_votes variable; which is dependent on the variable from the County_name list
        County_vote_count = county_votes[county_name] 
        # 6c: Calculate the percentage of votes for the county.
        # Establishing the vote percentage formula.  Using the county vote count
        county_vote_percentage = (County_vote_count)/(total_votes)*100
         # 6d: Print the county results to the terminal.
         # Here we are printing the results of the county data we have just calculated.  Using an f-line structure we are printing the county_name, county_vote_percentage; and the county_vote_counts lists.  Furthermore we are printing them in order, with formatting and each county being on its own line.
        print(f'{county_name}: {county_vote_percentage:.1f}% ({County_vote_count:,})\n')
         # 6e: Save the county votes to a text file.
         # iteration on the above print code, but adapting to write the same output into the txt_file
        txt_file.write(f'{county_name}: {county_vote_percentage:.1f}% ({County_vote_count:,})\n')
         # 6f: Write an if statement to determine the winning county and get its vote count.
         # Beginning the if statement to account for the winning county, winning county count & winning county percentage variables.
            #Both of the following statements must be true in order for variables after the statements to be accounted for
        if (County_vote_count > winning_county_vote) and (county_vote_percentage > winning_county_percentage):
            #The largest county will be equal to ONE of the 'county name' variables we added into the county_options dictionary back in step 3.  
            #The way that county name is determined is by using the 2 if statements above: so that only the county with BOTH the largest number of votes and largest vote percentage will be identified as the largest county
            largest_county = county_name
            #The winning county vote variable will be equal to the county vote calculation determeined in the first if statement equation
            winning_county_vote = County_vote_count
            #The winning county percentage variable will be equal to the county vote percentage calculation determeined in the second if statement equation
            winning_county_percentage = county_vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    # Creating a variable that consists of the formatting and largest county infomration
    largest_county_results = (
        # each of the \n variables establishes a new line break within the text.  So each of the following items are listed on seperate lines
        (f"\n-------------------------\n"
        f'Largest County Turnout: {largest_county}\n'
        f"-------------------------\n"))
    # printing the largest county results to the terminal
    print(largest_county_results)

    # 8: Save the county with the largest turnout to a text file.
    # saving the largest county results formatting and information to the txt_file. 
    txt_file.write(largest_county_results)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
