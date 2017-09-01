# Steps
# 1. Take the input from user as which data file he/she needs to process. File list (available to process) is saved in a dictionary and stored under raw_data directory.
# 2. Read csv data and iterate through it to create the date, revenue & revenue change data lists
# 3. Perform the operations on the list data for the required analysis.
# 4. Store the string to print into a variable.
# 5. Print the string onto terminal and write the same into a file. Filename is dynamically created using the input file number.

#import the required modules
import csv
import datetime
import time
import os

#dictionary of input data files to provide a choice for user to process a specific file
inpFileDict = { 1: 'budget_data_1.csv', 2: 'budget_data_2.csv'}

#take user input to select a specific file for processing
choice = input("Please choose a number to process the corresponding file:- " + str(inpFileDict) + " :")

#setting input and output filenames
filename=inpFileDict[int(choice)]

#file paths
inputFilePath = os.path.join("raw_data", filename)
outFilePath = os.path.join("analysis", "BudgetAnalysis_"+choice+".txt")

#lists to store the data
dtLst, rvnLst, rvnChg = [], [], []

#read csv into an object for further processing
with open(inputFilePath) as csvfile:

    #using csv reader method, read the content of each row into an object (list)  
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header line
    next(csvreader)

    #add content of each column into seperate lists
    for row in csvreader:
        dtLst.append(row[0])
        rvnLst.append(int(row[1]))
        
    #add revenue change figures into a new list
    rvnChg.append(rvnLst[0])
    for i in range(1,len(rvnLst)):
        rvnChg.append(rvnLst[i] - rvnLst[i-1])

#creating a string of statements to print
printVar = ("\n==========" + "\n" +
            "Financial Analysis" + "\n" +
             "------------------" + "\n" +
             "Total Months:" + str(len(dtLst)) + "\n" +
             "Total Revenue: $" + str(sum(rvnLst)) + "\n" +
             "Average Revenue Change: $" + str(int((sum(rvnLst))/len(rvnLst))) + "\n" +
             "Greatest increase in Revenue: "+str(dtLst[rvnChg.index(max(rvnChg))])+" $" + str(max(rvnChg)) + "\n" +
             "Greatest decrease in Revenue: "+str(dtLst[rvnChg.index(min(rvnChg))])+" $" + str(min(rvnChg)) + "\n" +
             "------------------") 

#printing the results on terminal
print(printVar)

#writing the results into a text file
with open(outFilePath, 'w') as txt_file:
    txt_file.write(printVar)
