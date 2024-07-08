'''
Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
'''

# Given ex. abc and cba -> true
# Given ex. aaa and cba -> false
# Given ex. aac and cca -> false - Cannot use set bc of this edge case
# Given ex. aabbcc and cba -> false
# Given ex. '' and cba -> false
# Given ex. abcdefg and abcgefd -> true
# Given ex. None and abcgefd -> raise error

from collections import Counter

def check_permutation_sorted(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Values must be strings")
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

    # run time is O(n log (n))
    # space is O(1) 


def check_permutation_dict(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Values must be strings")
    if len(s1) != len(s2):
        return False
    counter_dict = {}
    for x in range(len(s1)):
        char_1 = s1[x]
        char_2 = s2[x]
        if counter_dict.get(char_1):
            counter_dict[char_1] += 1
        else:
            counter_dict[char_1] = 1
        if counter_dict.get(char_2):
            counter_dict[char_2] -= 1
        else:
            counter_dict[char_2] = -1
    for count in counter_dict.values():
        if count != 0:
            return False
    return True

    # Could rearrange to do two for-loops with bail out on second loop, but looping on identical lengths and looping on lookup seems the same as looping on str1 and str2 
    # run time is O(n))
    # space is O(1) 

# Aha - interesting idea leveraging list instead of dict
def check_permutation_list(s1, s2, max_char=256):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Values must be strings")
    if len(s1) != len(s2):
        return False
    counter_list = [0] * max_char # Essentially creating a lookup based on the max chars in unicode/ascii using indices for lookup rather than keys
    for char_1 in s1:
        counter_list[ord(char_1)] += 1
    for char_2 in s2:
        # We have already hit 0 for this char and are about to decrement again in this current iteration, so bail now
        # Saves us from waiting for another case, or having to loop again looking for 0
        if counter_list[ord(char_2)] == 0:
            return False
        counter_list[ord(char_2)] -= 1
    return True

    # run time is O(n))
    # space is O(1) only ever max length of unicode/ascii



def check_permutation_counter(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Values must be strings")
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

    # run time is O(n))
    # space is O(1) 


# Remember set is not viable for this problem/only counter due to the edge case of aaaab and abbbb (same length, same letters, wrong count though - not pure permutation)
# Timeit shows set() equality check being more performant than Counter() equality check, if only set would work here
