import os
import csv

# This variable will store the results
results = []

# This variables will store the data
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# The file to the CSV file to read it
file_path=os.path.join(".","resources","election_data.csv")

with open(file_path) as my_file:
    csv_iterable=csv.reader(my_file)
    header = next(csv_iterable ) # To skip the header line

    # We iterate over each line in the csv file
    for line in csv_iterable:
        fields = line
        voter_id, county, candidate = fields # We extract the voter's information
        total_votes += 1 # We count the total number of votes
        if candidate in candidates: # We count votes for each candidate
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# We calculate and store results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

# We determine who is the winner
for candidate, votes in candidates.items():
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# This is a summary of the results that we will print
summary = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
] + results + [
    "-------------------------",
    f"Winner: {winner['name']}",
    "-------------------------",
]

# We print the summary to the terminal
for line in summary:
    print(line)

# We export the summary to a .txt file
with open('election_results.txt', 'w') as output_file:
    for line in summary:
        output_file.write(line + '\n')

print("Results have been exported to 'election_results.txt'.")
