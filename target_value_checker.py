# Write a Python function that takes a sorted list of numbers and a target value as input and returns the index of the target value if found, otherwise returns -1 (Please use binary search) 

def target_value_checker(sorted_list, target):
    """
    This function performs a binary search on a sorted list to find the index of a target value.
    
    :param sorted_list: List[int] - A sorted list of integers.
    :param target: int - The target value to search for.
    :return: int - The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
