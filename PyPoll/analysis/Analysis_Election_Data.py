import os

#set the path for the file
csvpath = os.path.join("..", "Resources", "Resources_election_data.csv")

#open the csv
import csv

with open(csvpath,) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #skip header row
    csv_header = next(csv_file)

#print(csv_header)

#assign my empty dictionaries
    voter = []
    county = []
    candidates = []
    candidates_votes = {}
    vote_count = []
    winner_votes = 0
#each row
    for rows in csv_reader:
        voter.append(rows[0])
        if rows[2] not in candidates:
            candidates.append(rows[2])
            candidates_votes[rows[2]] = 0
        candidates_votes[rows[2]] += 1


#total votes
total_votes = len(voter)

#print results
print("\nElection Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes:,}")
print("-----------------------------------")
for candidate in candidates:
    if candidates_votes[candidate] > winner_votes:
        winner = candidate
        winner_votes = candidates_votes[candidate]

    print(f'{candidate}: {candidates_votes[candidate]/total_votes*100:.3f}% ({candidates_votes[candidate]:,})')

print("-----------------------------------")
print(f'Winner: {winner}'+ "\n")
print("-----------------------------------")


#output to a txt file
f = open("analysis_election_data.txt", "w")
f.write("\nElection Results" + "\n")
f.write("-----------------------------------" + "\n")
f.write(f"Total Votes: {total_votes:,}" + "\n")
f.write("-----------------------------------" + "\n")
for candidate in candidates:
    if candidates_votes[candidate] > winner_votes:
        winner = candidate
        winner_votes = candidates_votes[candidate]

    f.write(f'{candidate}: {candidates_votes[candidate]/total_votes*100:.3f}% ({candidates_votes[candidate]:,})' + "\n")

f.write("-----------------------------------" + "\n")
f.write(f'Winner: {winner}' + "\n")
f.write("-----------------------------------" + "\n")

f.close()

# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
