import os
import csv

pyBankCSV= os.path.join('Input/budget_data.csv')

Change = 0
rows = 0
Total_PL = 0
Total_Change = 0
Prior_M = 0
Max = ["Date", 0]
Min = ["Date", 0]

with open (pyBankCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        rows = rows + 1
        if rows > 1:
            Total_PL = Total_PL + int(row[1])
            if rows > 2:
                Total_Change = Total_Change + (float(row[1])-Prior_M)
                Change = (float(row[1])-Prior_M)
                if Change > Max[1]:
                    Max = [row[0],Change]
                if Change < Min[1]:
                    Min = [row[0],Change]
            Prior_M = float(row[1])
            
    print("Total Months: " + str(rows - 1))
    print("Total Profit/Loss: $" + str(Total_PL))
    print("Average Change: $" + str(round(Total_Change/(rows-2),2)))
    print("Greatest Increase in Profits: " + str(Max[0]) + " $" + str(Max[1]))
    print("Greatest Decrease in Profits: " + str(Min[0]) + " $" + str(Min[1]))
    
output = os.path.join('Output/pybankPREVOST.txt')
with open(output, 'w', newline='') as txtfile:

    # Write the first row
    txtfile.write("Total Months: " + str(rows - 1)+"\n")
    # Write the second row
    txtfile.write("Total Profit/Loss: $" + str(Total_PL)+"\n")
    #Write third row
    txtfile.write("Average Change: $" + str(round(Total_Change/(rows-2),2))+"\n")
    #Write fourth row
    txtfile.write("Greatest Increase in Profits: " + str(Max[0]) + " $" + str(Max[1])+"\n")
    #Write fifth row
    txtfile.write("Greatest Decrease in Profits: " + str(Min[0]) + " $" + str(Min[1]) +"\n")