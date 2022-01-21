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

# Initilize total votes variable and set to zero
total_votes = 0

# Initialize a list for the candidate names
candidate_options = []

# Initialize the dicionary to count votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    print(election_data)

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Retrieve and print the header row
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        #Add to total vote count
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the name to the options list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


# 1. The total number of votes cast
print(total_votes)

# 2. A complete list of candidates who received votes
print(candidate_options)

# 3. Print candidate vote dictionary
print(candidate_votes)

# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
