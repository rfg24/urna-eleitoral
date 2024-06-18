# Get the total number of voters
total_voters = int(input("Enter the total number of voters: "))

# Initialize votes for each candidate
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0

# Loop through each voter
for i in range(total_voters):
    print(f"Voter {i+1}, please enter your vote (1, 2, or 3): ")
    vote = int(input())
    if vote == 1:
        candidate1_votes += 1
    elif vote == 2:
        candidate2_votes += 1
    elif vote == 3:
        candidate3_votes += 1
    else:
        print("Invalid vote. Please try again.")

# Display the results
print("Election Results:")
print(f"Candidate 1: {candidate1_votes} votes")
print(f"Candidate 2: {candidate2_votes} votes")
print(f"Candidate 3: {candidate3_votes} votes")