# Problem 2: File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
An example `testdir` provided was added to this project folder in order to test our code.
Here is the example test directory listing:
```bash
./testdir
├── subdir1
│   ├── a.c
│   └── a.h
├── subdir2
├── subdir3
│   └── subsubdir1
│       ├── b.c
│       └── b.h
├── subdir4
├── subdir5
│   ├── a.c
│   └── a.h
├── t1.c
└── t1.h
```

## Reasoning Behind Decisions:

Given that we need to recursively search through a directory and any number of subdirectories for a file with specified suffix, I implemented the use of a recursive function to achieve this. Specifically, the function calls itself on every subdirectory it finds. The best conceivable runtime for this problem is `O(N)` where **N** represents the total number of files and directories in the entire directory tree starting from the root path passed into our function. This is true since we must examine every file at least once to determine if it matches the suffix criteria.

## Time Efficiency:
Time efficiency is `O(N)`

- **N** represents the total number of files and directories in the entire dicrectory tree starting at the root path
- The function visits each file and directory exactly once through the recursive traversal
- For each item, it performs constant-time operations

Since every file and directory in the tree must be examined exactly once, and each examination takes constant time, the overall time complexity is `O(N)`

## Space Efficiency:
In the worst-case scenario where the directory tree is very deep and all files match the suffix, the space eficiency is `O(N)`.