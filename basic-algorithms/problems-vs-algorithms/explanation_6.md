<!--
Problem 6: Unsorted Integer Array

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Problem 6: Unsorted Integer Array

This problem does not require any sorting algorithm and is performed in `O(n)` time complexity with `O(1)` space complexity. There isn't much to this solution to explain. You simply save the first integer as both the max_val and the min_val, then compare each number to this initial value and saving the this number in the appropriate variable as you iterate through each item in the array. By the end, you're left with the min and max values required, and it's done in a single traversal with no need for sorting.

