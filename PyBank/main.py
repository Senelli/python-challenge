import os
import csv
# Set path for file
csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

months = []
profits = []

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        months.append(row[0])

        # Add population
        profits.append(int(row[1]))
    
    max = 0
    min = 0
    for i in range(len(profits) - 1) :
        #if i + 1 < len(profits):
        diff = profits[i + 1] - profits[i] 
        if diff < min:
            min = diff
            min_index = i + 1
        if diff > max:
            max = diff
            max_index = i + 1
    print(len(months))
    print(sum(profits))
    print(months[max_index])
    print(max)
    print(months[min_index])
    print(min)