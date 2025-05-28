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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re

# tot_calls used as a counter to account for all calls made from Bangalore
tot_calls = 0
# to_bangalore_calls used as a counter to track all calls made from Bangalore to Bangalore
to_bangalore_calls = 0
# create an empty list to contain all the receiver calls area codes when calls are made from Bangalore
area_codes = set()

for call in calls:
    if call[0].startswith("(080)"):
        tot_calls += 1 # increment tot_calls by 1
        receiver = call[1]
        
        if receiver.startswith("("):
            # Use a regular expression to extract the numbers between parentheses
            match = re.search(r'\((\d+)\)', receiver) 
            code = match.group(1) # Extract the matched group
            area_codes.add(code)
            if code == "080":
                # Calls from Bangalore to Bangalore, therefore we increment to_bangalore_calls counter
                to_bangalore_calls += 1
        # test if a space " " is found in the receiver number i.e. it's a mobile number
        elif " " in receiver:
            area_codes.add(receiver[:4]) # add the first 4 digits of the mobile phone number as the prefix
        # else it isn't a mobile or a fixed line number, and in this exercise we are left with just telemarketers number
        # that start with 140
        else:
            if receiver[:3] == "140":
                area_codes.add("140")
    
unique_codes = sorted(area_codes)

# percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore, rounded to two decimal places
percent = round(((to_bangalore_calls / tot_calls) * 100), 2)

print("The numbers called by people in Bangalore have codes:")
for code in unique_codes:
    print(code)

print(f"{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


