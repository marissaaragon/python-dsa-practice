# Instructions:
# HT: Two Sum (⚡Interview Question) two_sum()
# Problem: Given an array of integers nums and a target integer target,
# find the indices of two numbers in the array that add up to the target.
# Input: A list of integers nums. An integer target.
# Output: A list of two integers representing the indices of the two numbers in the input array nums
# that add up to the target. If no two numbers in the input array add up to the target,
# return an empty list [].

def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return []

print ( two_sum([2, 7, 11, 15], 9) )
print ( two_sum([3, 2, 4], 6) )
print ( two_sum([3, 3], 6) )
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )
