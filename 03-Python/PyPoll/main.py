# Steps
# 1. Take the input from user as which data file he/she needs to process. File list (available to process) is saved in a dictionary and stored under raw_data directory.
# 2. Read csv data and iterate through it to create the candidate list and count the votes for each candidate
# 3. Maintain 2 lists: 1 each for candidate name and another for his/her votes. Keep incrementing vote count the list for vote counts. Maintain the same index for the corresponding value in both the lists.
# 4. Store the string to print into a variable.
# 5. Print the string onto terminal and write the same into a file. Filename is dynamically created using the input file number.

#import the required modules
import csv
import os

#dictionary of input data files to provide a choice for user to process a specific file
inpFileDict = { 1: 'election_data_1.csv', 2: 'election_data_2.csv'}

#take user input to select a specific file for processing
choice = input("Please choose a number to process the corresponding file:- " + str(inpFileDict) + " :")

#setting input and output filenames
filename=inpFileDict[int(choice)]

#file paths
inputFilePath = os.path.join("raw_data", filename)
outFilePath = os.path.join("results", "PollResults_"+choice+".txt")

#open the csv files and using csv reader method create the list objects to iterate through the data
with open(inputFilePath, 'r') as wb1:
  reader1 = csv.reader(wb1)
  wb1_list = list(reader1)

#creating blank list to store candidate names & corresponding votes.
canList, voteCt = [], []
    
#iterating through the data of 'election_data_1.csv' and adding the Candidate Names and corresponding vote count into the respective lists
for i in range(1,len(wb1_list)):
    if wb1_list[i][2] not in canList:
        canList.append(wb1_list[i][2])
        voteCt.append(1)
    elif wb1_list[i][2] in canList:
        voteCt[canList.index(wb1_list[i][2])] = voteCt[canList.index(wb1_list[i][2])] + 1

#assigning total vote count into a variable for further use
# totVotes = sum(voteCt)

#creating variable to store the string to print the data into file & terminal
indResults = ""
for k in range(len(canList)):
    indResults += str(canList[k]) + " : " + str(round((voteCt[k]/sum(voteCt) * 100),1)) + "% " + str(voteCt[k]) + "\n"

finalResults = (
    "\n=======================================\n" +
    "Election Results\n" +
    "-------------------------\n" +
    "Total Votes: " + str(sum(voteCt)) + "\n" +
    "-------------------------\n" +
    indResults + 
    "-------------------------\n" +
    "Winner: " + str(canList[voteCt.index(max(voteCt))]) + "\n" +
    "=======================================\n")

#printing the results on terminal
print(finalResults)

#writing the results into a text file
with open(outFilePath, 'w') as txt_file:
    txt_file.write(finalResults)
