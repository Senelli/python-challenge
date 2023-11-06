import os
import csv
# Set path for file
csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Setting up two lists to store months and profits
months = []
profits = []

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    # Reading the headers on the csv file
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # Add data in the months column to the months list
        months.append(row[0])

        # Add data in the profits column to the profits list
        profits.append(int(row[1]))

# closing the csv file 
csvfile.close()

# Initializing max and min values for finding the greatest increase and decrease in profits
max = 0
min = 0
# Initializing the total changes in profits
total_diff = 0
# Looping through the profits list
for i in range(len(profits) - 1) :
    # Finding the difference in profits
    diff = profits[i + 1] - profits[i] 
    # if the difference is less than the current minimum
    if diff < min:
        # new minimum is the current diffence
        min = diff
        # get the index of the current differnce
        min_index = i + 1
    # if the difference is more than the current maximum
    if diff > max:
        # new maximum is the current diffence
        max = diff
        # get the index of the current differnce
        max_index = i + 1
    # adding up the differences
    total_diff = total_diff + diff

# find the total months
total_months = len(months)

# find the total/net profits
total = sum(profits)

# find the average difference in the profit changes
average_diff = round(total_diff / (total_months - 1), 2)

# find the month with the greatest increase in profits
highest_month = months[max_index]

# find the month with the greatest decrease in profits
lowest_month = months[min_index]

# Specify the file to write to
output_path = os.path.join("analysis", "results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write the content on to a text file
    txtfile.write('Financial Analysis \n\n')

    txtfile.write('---------------------------- \n\n')

    txtfile.write('Total Months: ' + str(total_months) + '\n\n')

    txtfile.write('Total: $' + str(total) + '\n\n')

    txtfile.write('Average Change: $' + str(average_diff) + '\n\n')

    txtfile.write('Greatest Increase in Profits: ' + highest_month + '($' + str(max) + ') \n\n')

    txtfile.write('Greatest Decrease in Profits: ' + lowest_month + '($' + str(min) + ') \n\n')

# open the output file in read mode
with open(output_path, 'r') as txtfile:
    
    # read the output file on to the console
    print(txtfile.read())

# close the output file
txtfile.close()