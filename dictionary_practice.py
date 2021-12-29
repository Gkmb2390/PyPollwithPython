counties_dict={"arapahoe":422829, "denver":463353, "jefferson":432438}

#for county in counties_dict:
 #   print(counties_dict.get(county))

#for county in counties_dict.keys():
 #   print(county)

#for voters in counties_dict.values():
 #   print(voters)

#for county, voters in counties_dict.items():
 #   print(county,"county has",voters,"registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county had {voters:,} registered voters")