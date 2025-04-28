"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# Create an empty dictionary to fill with all telephone numbers as key, and length of time on phone (in seconds) as the value
phone_time = {}

for record in calls:
    num1 = record[0]
    num2 = record[1]
    duration = int(record[3])
    phone_time[num1] = phone_time.get(num1, 0) + duration
    phone_time[num2] = phone_time.get(num2, 0) + duration

phone_with_max_length = max(phone_time, key=phone_time.get)

print(f"{phone_with_max_length} spent the longest time, {phone_time[phone_with_max_length]} seconds, on the phone during September 2016.")
