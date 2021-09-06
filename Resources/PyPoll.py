# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# pri(nt the present time
print("The time now is ", now)
# Assign a variable for a file to load and a path
file_to_load = 'election_results.csv'
# Open the election results and read the file.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #read and print the header row.
    headers = next(file_reader)
    print(headers)

    
    















    



#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received the votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of the election based on popular vote
