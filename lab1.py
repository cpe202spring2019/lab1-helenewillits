

# finds the max of a list of numbers
# returns the value of the max(not the index)
# raises ValueError if the list is None
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:
        raise ValueError
    if not int_list:
        return None
    max_index = 0
    for i in range(len(int_list)):
        if int_list[i] > int_list[max_index]:
            max_index = i
    return int_list[max_index]


# recursively reverses a list of numbers
# returns the reversed list
# raises ValueError if list is None
def reverse_rec(int_list, n=0):  # must use recursion
    # n counts up and len(int_list)-(n+1) counts down until they meet
    if int_list is None:
        raise ValueError
    if n >= len(int_list) - (n + 1):
        return int_list
    last_val = int_list[len(int_list) - (n + 1)]  # stores the last value in the section of sorted list we are using
    int_list[len(int_list) - (n + 1)] = int_list[n]  # makes the last one equal to the first one
    int_list[n] = last_val  # makes the first one equal to the last one
    return reverse_rec(int_list, n + 1)


# searches for target in int_list[low..high]
# returns index if found
# returns None if target is not found
# raises ValueError if list is None
def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if low < 0 or high >= len(int_list):
        raise IndexError

    center_index = int(((high - low) / 2) + low)  # center or center.floor

    if int_list[center_index] == target:  # base case : finds the target value
        return center_index

    if low >= high:  # base case : searches all values, target value not in list
        return None  # already checked the == value as a target

    if int_list[center_index] < target:                           # implements the recursion
        return bin_search(target, center_index + 1, high, int_list)
    else:
        return bin_search(target, low, center_index - 1, int_list)
