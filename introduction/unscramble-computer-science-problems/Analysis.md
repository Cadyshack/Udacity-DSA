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


## Task2


## Task3


## Task4


**Description**: The problem involves calculating the sum of all elements in an integer array.

**Approach**: Iterated through the array a single time, summing each element.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of the array once.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the array.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.