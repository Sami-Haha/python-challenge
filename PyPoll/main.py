#Python Challenge - PyPoll script
#Analyse the votes and calculate; the total number of votes cast,
# a complete list of candidates who received votes and percentage won,
# the winner of the election

#import modules to assist python in reading and writing files.
import os
import csv
import collections
#define path to input file
Polling_csv = os.path.join("Resources", "election_data.csv")
#define path to output file
out_file = os.path.join("Analysis", "Analysis.txt")

#create dictionary counting candidate votes using collection.Counter on Candidates.
Candidates = collections.Counter()

#Open and read csv
with open(Polling_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    csv_header = next(csv_file)
    
   #Read through each row of the data after the header and create a counter dictionary of Candidates
   #With the candidates names as the key and vote count as values.
    for row in csv_reader:
       Candidates [row[2]] += 1

#Create a list of candidates from the dictionary using the key.
Candidate_List = list(Candidates.keys())

#Extract the number of votes the candidates received from the Dictionary.
Vote_List = list(Candidates.values())

#Create an empty list for the percentage vote count
Percent_Vote_List = []

#Create variable for the total number of votes counted.
Total_votes = Candidates.total()

#Create variable for the winner, using '.most_common' and then just the name. 
Winner_List = list(Candidates.most_common(1))
Winner_S = Winner_List[0]
Winner = Winner_S[0]
#Get percentage values of results. Using a for loop and parse to new list.
for x in Vote_List:
    temp = x / Total_votes * 100
    Percent_Vote_List.append(temp)

#Zip lists together ready for printout
Combined_Results = list(zip(Candidate_List, Percent_Vote_List, Vote_List))

#Create output
header = ['Election Results']
output_results = [
    ['--------------------------------'],
    ['Total Votes:    ', Total_votes],
    ['--------------------------------'],
    [Combined_Results],
    ['---------------------------------'],
    ['Winner:    ',Winner]
    
    ]

# print the results to the terminal
print("-" * 40)
print("Election Results")
print("-" * 40)
print("Total Votes:    ", Total_votes)
print("-" * 40)
for row in Combined_Results:
    print(row)
print("-" * 40)
print ("Winner:      ", Winner)
print("-" * 40)


#Print the results to a test file called "Analysis.txt"
#  Open the output file
with open(out_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    #write the header
    writer.writerow(header)
    #write the output
    writer.writerows(output_results)



