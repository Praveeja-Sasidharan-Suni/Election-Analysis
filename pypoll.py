#Importing the dependencies and modules

import os
import csv
#The data we need to retrieve
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)
    # 1. Initialize a total vote counter.
    total_votes = 0

    #Creating a text file to save the results
    file_to_save=os.path.join("analysis","Election_Analysis.txt")
    #open(file_to_save, "w")
    with open(file_to_save, "w") as txt_file:
        # Write three counties to the file.
        txt_file.write("Counties in the Election\n")
        txt_file.write("--------------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson")
   
        #Read and analyse the data here
        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
         # Print the header row.
        headers = next(file_reader)
        print(headers)
        # Print each row in the CSV file.
        for row in file_reader:
             #  Add to the total vote count.
                total_votes += 1

        # 3. Print the total votes.
        print(total_votes)


