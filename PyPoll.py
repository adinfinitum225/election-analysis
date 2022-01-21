import csv
import os
# The data we need to retrieve
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the file to write our data to
with open(file_to_save) as election_analysis:

    print(election_analysis)

# Open the election results and read the file
with open(file_to_load) as election_data:

    print(election_data)

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Retrieve and print the header row
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
