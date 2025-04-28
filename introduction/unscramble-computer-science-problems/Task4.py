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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# set an empty list to capture all the phone numbers making outgoing calls
out_calls = []
# set an empty list to capture all other numbers, sending text, receiving texts, receiving calls
other_nums = []

for record in calls:
    out_calls.append(record[0])
    other_nums.append(record[1])

for record in texts:
    other_nums.extend([record[0], record[1]])

unique_out_calls = set(out_calls)
unique_other_nums = set(other_nums)
# Find numbers in unique_out_calls that are not in unique_other_nums
telemarketers = unique_out_calls - unique_other_nums
# Convert the result back to a sorted list
telemarketers = sorted(telemarketers)

# Print the result
print("These numbers could be telemarketers:")
for number in telemarketers:
    print(number)