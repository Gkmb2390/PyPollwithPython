candidate_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("what is the total votes in the election?"))
message_to_candidate =(
    f"You recieved {candidate_votes:,} number of votes."
    f"The total numbers of votes in the elections was {total_votes:,}"
    f"You recieved {candidate_votes/total_votes*100:.2f}% of the total votes"
)
print(message_to_candidate)

#counties_dict={"arapahoe":422829, "denver":463353, "jefferson":432438}
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")