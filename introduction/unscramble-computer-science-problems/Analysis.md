### Note

Task0 - Task4 all use the same texts.csv and calls.csv file as input, where it reads those files and saves each line of those csv files as a list of lists, where each individual record is itself a list with the needed information about a specific call or text. When doing the following Compelexity Analysis for each task, I will ignore the input statements where we read and fill the texts and calls list. The Time Complexity of reading these files are $O(m + n)$ where there are $n$ records in the texts.csv and $m$ records in the calls.csv file. This would give a Big O approximation of $O(n)$ where $n$ is the total number of records read. The following analysis will disregard this part of the code in the analysis, since the task asks to analyze my given solutions, and this file reading is done exactly the same for all Tasks.

## Task0

**Description**: The task simply asks to print out the first record of texts and the last record of calls.

**Approach**: Stored the first record of text into a variable (first_text), and the last record of calls into another variable (last_call). Since the *texts* and *calls* list are lists of list, meaning the items in those lists are themeselves lists, it makes it easier to follow by explicitly saving the first and last record of those lists into their own variable to then print out the various items of the record.

**Complexity Analysis**:

- **Algorithm**: Access first record of text and last record of calls and print out the required information.
- **Big O Notation**: $O(1)$ .
- **Justification**: Accessing an element in a list by index is $O(1)$ and priting a string is $O(1)$. Therefore, the total time complexity function can be expressed as $O(4)$, which simplifies to $O(1)$. This just shows that this algorithm's runtime is constant and does not depend on the size of the input.

## Task1

**Description**: The problem involves counting the number of unique telephone numbers found in text.csv and calls.csv datasets.

**Approach**: Create an empty list (num_record) to save all telephone numbers, then iterate through both arrays (calls and texts) seperately, where we append the telephone numbers from each record to the *num_record* list. We then remove any duplicates by simply turning this list into a set (unique_numbers), and then printing out the `len(unique_numbers)` to get the total count of unique telephone numbers.

**Complexity Analysis**:

- **Algorithm**: Two seperate loops, one runs through *texts* list, and the other runs through the *calls* list. They both loop through each element of their respective list, and appends the 2 telephone numbers from each record into our *num_record* list. After these loops finish, we have every telephone number stored in our *num_record* list, but that includes duplicates. We get the unique numbers by turning this list into a set, and then print out the length of this set to get the total number of unique telephone numbers.
- **Big O Notation**: $O(n)$ where $n$ is the combined number of records from the texts and calls dataset.
- **Justification**: To be accurate, we can write Big O as $O(n + m)$ where $n$ is the number of texts elements, and $m$ is the number of elements in the calls list. The most expensive operation in this code is in converting the *num_record* list into a set, which can be approximated as $O(2n + 2m)$, since converting a list of size $k$ to a set has a time complexity of $O(k)$. Specifically, we pull two telephone numbers from each list item, giving us the $k = 2n + 2m$. In the end, $O(2n + 2m)$ simplifies to $O(n + m)$, which in turn simplifies to $O(n)$, since the runtime of the algorithm scales linearly with total size of records in the dataset, which in this case is split between two seperate datasets (*texts* and *calls*) lists.

## Task2

**Description**: The goal of this code is to determine which telephone number spent the longest time on the phone during the period of September 2016. All the records in the calls.csv are from September 2016, therfore we use this dataset to output the solution.

**Approach**: Iterated through the calls list to build a *phone_time* dictionary that stores phone numbers as keys and the total call duration in seconds as the value. For each record in the calls list, we extract two telephone numbers and the call duration and update the *phone_time* dictionary for both *num1* and *num2* using the `get()` method to retrieve the current value (or 0 if they key does not exist) and adds the *duration* to it.

**Complexity Analysis**:

- **Algorithm**: A single loop runs through each element of the *calls* list once.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the *calls* list.
- **Justification**: The for loop runs $n$ times, and each operations inside the loop are $O(1)$ since they simply update the dictionary via the `get()` method of a dictionary, therefore the total complexity for this loop is $O(n)$. We then use the `max()` function with the `key=phone_time.get` argument that retrieves the value for each key during the max() function iteration. Let $k$ be the number of unique phone numbers in the *phone_time* dictionary, then the max() function iterates through all $k$ keys, and for each key, the `get()` operation is performed, which is $O(1)$, which gives us a total complexity for this step of $O(k)$. Since $k$ (the number of unique phone numbers) is typically much smaller than $n$ (the number of call records), the $O(n)$ term dominates. Therefore, the overall time complexity is $O(n)$.

## Task3

**Description**: The goal of the code is to analyze calls made from fixed lines in Bangalore "(080)" and determine:

1. The unique area codes and mobile prefixes called by people in Bangalore.
2. The percentage of calls from Bangalore to Bangalore

**Approach**: Iterated through the *calls* list once, looking at each record to see if the call originated from Bangalore. If calls originated from Bangalore, then the area codes and mobile prefixes called are appended to the *area_code* list. We then get the unique area codes by turning the *area_code* list into a set, and then sorting the set using the `sorted()` function. For part B, we used two counters, *tot_calls* used to count total amount of calls coming from Bangalore, and *to_bangalore_calls* used to count the calls made from Bangalore to Bangalore. We then calculate the percentage of calls from Bangalore to Bangalore by getting the ratio of those two counters.

**Complexity Analysis**:

- **Algorithm**: A single loop runs through each element of the *calls* list once, then we use the python `sorted()` function to sort the set of unique area codes. We finish by calculating the percentage of calls from Bangalore to Bangalore by dividing (to_bangalore_calls / tot_calls).
- **Big O Notation**: $O(n\log(n))$ where $n$ is the number of elements in the array.
- **Justification**: The dominant terms are $O(n)$ (from iterating through the *calls* list) and $O(u\log(u))$ (from sorting the unique area codes). Since $u$ (the number of unique area codes) is typically much smaller than $n$ (the number of call records), the overall time complexity can be expressed as $O(n + u\log(u))$, but assuming a worst case scenario where every number of the *calls* list is a unique number, we would then get $O(n + n\log(n))$, which in turn simplifies to Big O of $O(n\log(n))$.

## Task4

**Description**: The task is to identify potential telemarketer numbers. A telemarketer is defined as a number that makes outgoing calls but never sends or receives texts, and never receives incoming calls.

**Approach**: Created two lists: *out_calls* to store numbers that make calls, *other_nums* to store numbers that either receive incoming calls or send/receive texts. Iterated through the *calls* dataset to populate the *out_calls* with every number making a phone call, and *other_nums* lists with all telephone numbers receiving a phone call. Similarly, iterated through the *texts* dataset to further populate the *other_nums* list by adding all phone numbers that either send or receive texts. Created two sets from these two lists to obtain the unique numbers of each (*unique_out_calls* and *unique_other_nums*). We then identified telemarketer numbers by subtracting *unique_other_nums* set from *unique_out_calls* set. Finally, we sorted the resulting set of telemarketer numbers and printed them.

**Complexity Analysis**:

- **Algorithm**: Two loops iterate through the *calls* and *texts* datasets to populate the lists. Each list is then turned into a set to get only the unique numbers. A set subtraction operation is performed to identify telemarketer numbers, followed by sorting the resulting set.
- **Big O Notation**: $O(n\log(n))$, where $n$ is the number of call records in the *calls* dataset.
- **Justification**: Iterating through the *calls* and *texts* datasets is $O(n + m)$. Set operations like union and subtraction are $O(a + b)$, where $a$ and $b$ are the sizes of the sets involved, which are subsets of $n$ and $m$. Sorting the telemarketer numbers is $O(k\log(k))$, where $k$ is the number of unique numbers remaining from the subtracting the two sets. In a worst case scenario, every outgoing call would be a unique telemarketer number, which in turn would make $k$ = $n$ when sorting the telemarketer number making the `sorting()` function have a time complexity of $O(n\log(n))$. Since $O(n\log(n))$ is a much faster growth rate compared to $O(n)$, we simplify our worst case Big O notation to simply be $O(n\log(n))$.
