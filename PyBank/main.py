#Python Challenge - PyBank script
#Analyse financial records for net Profit/Loss over a time period,
# provide the average change, greatest increase and greatest decrease.

#import modules to assist python in reading and writing files.
import os
import csv
#define path to input file
Budget_csv = os.path.join("Resources", "budget_data.csv")
#define path to output file
output_file = os.path.join("Analysis","Analysis.txt")

#set initial variables
Total_months = 0
Net_total = 0
# Profit/Losses abbreviated to PL
starting_PL_value = 0
final_PL_value = 0
PL_change = 0
Average_PL = 0
Increase_PL = 0
Decrease_PL = 0
Date_Increase_PL = 0
Date_Decrease_PL = 0
row_num = 1

#Open and read csv
with open(Budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    csv_header = next(csv_file)

    #Read through each row of the data after the header. 
    # Set the variables to equal the values of the current row.
    for row in csv_reader:
        Net_total += int(row[1])
        Total_months += 1
        final_PL_value = int(row[1])
        Test_value = int(row[1])
        Date_test = str(row[0])
        # Read and store opening Profit/Loss value
        if row_num == Total_months:
            starting_PL_value = int(row[1])            
        #Test to find the greatest value of profit and also save the date.
        if Increase_PL < Test_value:
            Increase_PL = int(row[1])
            Date_Increase_PL = Date_test
        # Test to find the greatest loss for the period and also save the date.    
        if Decrease_PL > Test_value:
            Decrease_PL = int(row[1])
            Date_Decrease_PL = Date_test
       
    # Find the average change from first PL value to last PL value for the period.
    Average_PL = (final_PL_value - starting_PL_value)/Total_months        

#Create output
header = [['Financial Analysis'],
          ['---------------------------']]
output_results = [
    ['Total Months:    ', Total_months],
    ['--------------------------------'],
    ['Total:    ', Net_total],
    ['Average Change:    ', Average_PL],
    ['Greatest Increase in Profits:    ', Date_Increase_PL, '    ',"$",Increase_PL],
    ["Greatest Decrease in Profits:   ", Date_Decrease_PL, "    ", "$",Decrease_PL]
]

# print the results to the terminal
print(*header)
for s in output_results:
    print(*s)
# Print the results to a test file called "Analysis.txt"
#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    #write the header
    writer.writerows(header)
    #write the output
    writer.writerows(output_results)



