"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Create an empty list to use to combine all numbers from texts and calls
num_record = []
# Loop through text records and add the telephone numbers to num_record, which are the first and second items of each record
for record in texts:
    num_record.append(record[0])
    num_record.append(record[1])

# Loop through the calls list and add the telephone numbers to num_record, which are the first and second items of each call record
for record in calls:
    num_record.append(record[0])
    num_record.append(record[1])

# get the unique numbers
unique_numbers = set(num_record)

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")