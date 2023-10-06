import os
import csv

# This variable will store the results
results = []

# This variables will store data
num_months = 0
net_total = 0
changes = []
max_increase = 0
max_increase_date = None
max_decrease = 0
max_decrease_date = None
prev_profit_losses = None

# The file to the CSV file to read it
file_path=os.path.join(".","resources","budget_data.csv")

with open(file_path) as my_file:
    csv_iterable=csv.reader(my_file)

    header = next(csv_iterable ) # To skip the header line

    # We iterate over each line in the csv file
    for line in csv_iterable:
        date, profit_losses = line
        profit_losses = int(profit_losses)

        # PART 1: Count the number of months
        num_months += 1

        # PART 2: Calculate the net total amount
        net_total += profit_losses

        # PART 3: Calculate changes and average change
        if prev_profit_losses is not None:
            change = profit_losses - prev_profit_losses
            changes.append(change)
        
        # PART 4: Find the greatest increase in profits
        if prev_profit_losses is not None and change > max_increase:
            max_increase = change
            max_increase_date = date
        
        # PART 5: Find the greatest decrease in profits
        if prev_profit_losses is not None and change < max_decrease:
            max_decrease = change
            max_decrease_date = date

        prev_profit_losses = profit_losses

# We calculate the average change
average_change = sum(changes) / len(changes)

# We append the data to the results list
results.append(f'Number of months included in the dataset: {num_months}')
results.append(f'Net total amount of "Profit/Losses" over the entire period: {net_total}')
results.append(f'Changes in "Profit/Losses" over the entire period: {changes}')
results.append(f'Average change in "Profit/Losses" over the entire period: {average_change:.2f}')
results.append(f'The greatest increase in profits occurred on {max_increase_date} with an amount of ${max_increase}')
results.append(f'The greatest decrease in profits occurred on {max_decrease_date} with an amount of ${max_decrease}')

# We print the results on the terminal
for result in results:
    print(result)

# We export the results to a .txt file
with open('budget_data_results.txt', 'w') as output_file:
    for result in results:
        output_file.write(result + '\n')

print('Results have been both printed and exported to "budget_data_results.txt"')