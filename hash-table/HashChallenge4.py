# Instructions:
# HT: Group Anagrams (⚡Interview Question)
# You have been given an array of strings, where each string may contain only lowercase English letters.
# You need to write a function group_anagrams(strings) that groups the anagrams in the array together using
# a hash table (dictionary). The function should return a list of lists, where each inner list contains
# a group of anagrams.
# For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"],
# the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three
# strings are anagrams of each other, the next two strings are anagrams of each other,
# and the last string has no anagrams in the input array.
# You need to implement the group_anagrams(strings) function and return a list of lists,
# where each inner list contains a group of anagrams according to the above requirements.

def group_anagrams(strings):
    anagram_groups = {}

    for string in strings:
        canonical = ''.join(sorted(string))

        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]

    return list(anagram_groups.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )






