# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = []
        totals_lookup = {}
        for idx in range(len(strs)):
            total = 0
            for char in strs[idx]:
                total += hash(char)
                print(hash(char))
            if total in totals_lookup:
                groupings[totals_lookup[total]].append(strs[idx])
            else:
                groupings.append([strs[idx]])
                totals_lookup[total] = len(groupings) - 1
        return grouping




