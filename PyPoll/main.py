import os
import csv
# Set path for file
csv_path = os.path.join("Resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Setting up two lists to store unique candidates and data in the candidate column of the csv file
unique_candidates = []
votes = []

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    # Reading the headers on the csv file
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # Add data in the candidates column to the votes list
        votes.append(row[2])

# closing the csv file 
csvfile.close()

# Looping through the votes list
for i in votes :
    # check if exists in unique_candidates or not
    if i not in unique_candidates: 
        # Append candidate to the unique candidate list 
        unique_candidates.append(i)

# Initialize list for counting votes for each candidate
vote_count = []
# Initialize counter variable for counting votes for each candidate
count = 0
# Initialize variable for storing percentage of votes for each candidate
percentage = 0

# Loop through the list with the unique candidates
for i in unique_candidates:
    # Loop through the votes with all candidates
    for j in votes:
        # check if current candidate in the unique candidate is found in the list with all the votes with candidate names
        if i == j:
            # increment count to count the number of votes for the candidate
            count = count + 1
    # Append the vote count to a new list to with total votes for each candidate
    vote_count.append(count)
    # Set count to zero to start counting votes for a new candidate
    count = 0

# count the total votes 
total_votes = len(votes)
# create a dictionary with candidates and their vote count
voting_results = dict(list(zip(unique_candidates, vote_count*len(unique_candidates))))
# determine the winner by getting the key of the candidate with the maximum amount votes in the dictionary
winner = max(voting_results, key=voting_results.get)

# Specify the file to write to
output_path = os.path.join("analysis", "results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write the content on to a text file
    txtfile.write('Election Results \n\n')

    txtfile.write('---------------------------- \n\n')

    txtfile.write('Total Votes: ' + str(total_votes) + '\n\n')

    txtfile.write('---------------------------- \n\n')

    # write each candidate's in the dictionary along with their percentage of votes and their vote counts on to the text file
    for key in voting_results: 
        txtfile.write(key + ': ' + str(round(voting_results[key]/total_votes * 100, 3)) + '% (' + str(voting_results[key]) + ')' + '\n\n')

    txtfile.write('---------------------------- \n\n')

    txtfile.write('Winner: ' + winner + '\n\n')

    txtfile.write('---------------------------- \n\n')

# open the output file in read mode
with open(output_path, 'r') as txtfile:
    
    # read the output file on to the console
    print(txtfile.read())

# close the output file
txtfile.close()