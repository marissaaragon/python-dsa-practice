# Instructions:
# HT: Find Duplicates (⚡Interview Question)
# find_duplicates()
# Problem: Given an array of integers nums, find all the duplicates in
# the array using a hash table (dictionary).
# Input: A list of integers nums.
# Output:A list of integers representing the numbers in the input array nums that appear more than once.
# If no duplicates are found in the input array, return an empty list [].

def find_duplicates(arr):
    num_counts = {}
    duplicates = []

    for i in arr:
        if i in num_counts:
            num_counts[i] += 1
        else:
            num_counts[i] = 1

    for key in num_counts:
        if num_counts[key] > 1:
            duplicates.append(key)
    return duplicates


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""