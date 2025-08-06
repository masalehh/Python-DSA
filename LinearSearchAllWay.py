"""Linear Search Variants in Python

1. linear_search_all_indices: Finds all indices of a target value.
2. linear_search_case_insensitive: Finds a string target ignoring case.
3. linear_search_dict_list: Searches within a list of dictionaries by dict key.

Each function follows Python coding standards (PEP 8) and includes docstrings.
"""


from typing import List, Any 


def linearSearchAllOccurences(arr:List[Any], searchValue:Any) -> List[int]:
    """
    Returns all indices where the searchValue occurs in the list.

    Parameters:
        arr (list): The list to search.
        target (Any): The value to search for.

    Returns:
        list: List of indices where the searchValue is found. Return Empty if not found.
    """
    
    indices = [] 
    for i, value in enumerate(arr):
        if searchValue == value:
            indices.append(i) 
    return indices



def linear_case_insensative(arr:List[str], searchString:str) -> int:
    """
    Performs a case-insensitive linear search on a list of strings.

    Parameters:
        arr (list): List of strings to search.
        target (str): The string to search for.

    Returns:
        int: Index of the first match ignoring case, else -1.
    """
    searchString_lower = searchString.lower() 
    
    for i, string in enumerate(arr):
        if isinstance(string, str) and string.lower() == searchString_lower:
            return i 
    return -1 


def linear_search_in_dict(arr:List[dict], key:str, searchValue:Any) -> int: 
    """
    Searches for the first dictionary in a list where the given key matches the target.

    Parameters:
        arr (list): List of dictionaries.
        key (str): Dictionary key to search by.
        target (Any): Value to match.

    Returns:
        int: Index of the dictionary where key == target, else -1.
    """
    
    for i, item in enumerate(arr):
        if isinstance(item, dict) and item.get(key) == searchValue:
            return i 
    return -1 



# --------------------------
# 🔍 Example Usage
# --------------------------
if __name__ == "__main__":
    # Test 1: All Indices
    values = [10, 20, 30, 20, 40, 20]
    print("All Indices of 20:", linearSearchAllOccurences(values, 20))  # Output: [1, 3, 5]

    # Test 2: Case-Insensitive String Search
    words = ["Python", "Java", "C++", "PYTHON"]
    print("Case-Insensitive Search for 'python' at index:", linear_case_insensative(words, "python"))  # Output: 0
          
    # Test 3: Search in List of Dictionaries
    students = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    print("Search student by name 'Bob' at index:", linear_search_in_dict(students, "name", "Bob"))  # Output: 1
