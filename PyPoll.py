import csv
# Open a file for which a direct path is unknown use os module
# its allows interaction with operating system
import os
# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources/election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    
