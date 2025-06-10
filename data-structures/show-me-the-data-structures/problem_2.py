import os
from typing import Optional

def find_files(suffix: str, path: str) -> Optional[list[str]]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    output: list[str] = []

    try:
        list_dir = os.listdir(path)
    
        for item in list_dir:
            new_path = os.path.join(path, item)
            if os.path.isdir(new_path):
                sub_result = find_files(suffix, new_path)
                if sub_result is not None:
                    output.extend(sub_result)
            elif item.endswith(suffix):
                output.append(new_path)
        
        return output

    except FileNotFoundError:
        print(f"{path} is not a valid path!")


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    
    result = find_files(".c", "./testdir")
    expected_result = ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    assert result is not None and sorted(result) == expected_result, f"Failed: expected following array: {expected_result} \n instead returned {result}"
    print("Test Case 1 Passed: Standard directory structure")

    # Test Case 2: Searching for non existant file in directory
    no_file_result = find_files(".notfound", "./testdir")
    expected_result = []
    assert no_file_result == [], f"Failed: expected an empty list, returned {no_file_result} instead"
    print("Test Case 2 Passed: Searching for non existant file in drectory")
    
    # Test Case 3: Searching for a file in faulty directory path
    bad_path_result = find_files(".c", "./non_existent_folder/not_happening")
    assert bad_path_result == None, "Failed: expected `None` to be returned since FileNotFoundError exception raised"
    print("Test Case 3 Passed: Searching for a file in a faulty directory path")