print ("Election Analysis")
counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in counties")
else:
    print("Arapahoe and El Paso not in counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in counties")
else:
    print("Arapahoe and El Paso not in counties")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {
    "Arapahoe" : 422829,
    "Denver" : 463353,
    "Jefferson" : 432438    
    }

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438},]

for county_dict in voting_data:
    print(voting_data)

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict.values())

for county_dict in voting_data:
    for value in county_dict:
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
        print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
