import os

#set the path for the file
csvpath = os.path.join("..", "Resources", "Resources_budget_data.csv")

#open the csv
import csv

with open(csvpath,) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #this code was used because I didn't think I was reading the CSV file
    #line_count = 0
    #for row in csv_reader:
        #if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            #line_count +=1
        #else:
            #print(f'\t{row[0]} is the month and {row[1]} is the profit or loss')
            #line_count +=1
    #print(f'processed {line_count} lines')

    #skip header row
    csv_header = next(csv_file)

#print(csv_header)

#assign my rows / variables
    P_L = list()
    months = list()
    total_revenue = list()
    revenue_change = list()

#each row
    for rows in csv_reader:
        P_L.append(int(rows[1]))
        months.append(rows[0])

#total months
total_months = len(months)

#average revenue changes
for rev_chng in range (1, len(P_L)):
    revenue_change.append((int(P_L[rev_chng]) - int(P_L[rev_chng-1])))

revenue_average = sum(revenue_change) / len(revenue_change)

#Greatest increase and decrease in profits
greatest_increase = max(revenue_change)
greatest_decrease = min(revenue_change)

#print results
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(sum(P_L)))
print("Average Change: $" + str(round(revenue_average,2)))
print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " "($" + str(greatest_decrease) + ")")    

#output to a txt file
f = open("budget_data_analysis.txt", "w")
f.write("Financial Analysis" + "\n")
f.write("-------------------------" + "\n")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(sum(P_L)) + "\n")
f.write("Average Change: $" + str(round(revenue_average,2)) + "\n")
f.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " "($" + str(greatest_increase) + ")" + "\n")
f.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " "($" + str(greatest_decrease) + ")" + "\n")

f.close()