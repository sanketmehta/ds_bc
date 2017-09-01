# Steps
# 1. Take the input from user as which data file he/she needs to process. File list (available to process) is saved in a dictionary and stored under raw_data directory.
# 2. Read csv data and iterate through it to create the empId, firstName, lastName, dob, ssn, state data-lists while simultaneously performing the formatting of data
# 3. Add all the lists into a zip object.
# 4. Write the zip object into a csv file.

#import the required modules
import csv
import datetime
import os
from us_state_abbrev import * 

#dictionary of input data files to provide a choice for user to process a specific file
inpFileDict = { 1: 'employee_data1.csv', 2: 'employee_data2.csv'}

#take user input to select a specific file for processing
choice = input("Please choose a number to process the corresponding file:- " + str(inpFileDict) + " :")

#setting input and output filenames
filename=inpFileDict[int(choice)]

#file paths
inputFilePath = os.path.join("raw_data", filename)
outFilePath = os.path.join("output", "EmpData_"+choice+".csv")

#open the csv files and using csv reader method create the list objects to iterate through the data
with open(inputFilePath, 'r') as wb1:
  reader1 = csv.reader(wb1)
  wb1_list = list(reader1)

# #creating lists to store column data.
empId, firstName, lastName, dob, ssn, state = [], [], [], [], [], []

#iterating through the csv data list and saving the column data into individual lists
for j in range(1,len(wb1_list)):
    empId.append(wb1_list[j][0])
    firstName.append(wb1_list[j][1].split(' ',1)[0])
    lastName.append(wb1_list[j][1].split(' ',1)[1])
    dob.append(datetime.datetime.strptime(wb1_list[j][2], '%Y-%m-%d').strftime('%d/%m/%Y'))
    ssn.append(wb1_list[j][3].replace((wb1_list[j][3])[:6],'***-**'))
    state.append(us_state_abbrev.get(wb1_list[j][4]))

#adding the lists into a zipped object
csvout = zip(empId,firstName,lastName,dob,ssn,state)

#writing to a csv using the zipped object
with open(outFilePath, "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    writer.writerows(csvout)
