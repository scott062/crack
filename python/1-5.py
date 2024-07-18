# One away
test_1 = ("ple", "pale") # True 
test_2 = ("ple", "aple") # True 
test_3 = ("ple", "plea") # True 
test_4 = ("ple", "ple") # True 
test_5 = ("bake", "baking") # False 
test_6 = ("bake", "coke") # False 
test_7 = ("baker", "coke") # False 
test_8 = ("baker", "caker") # False 
'''
def one_away(string_one, string_two):
    if string_one == string_two:
        return True
    length_1 = len(string_one)
    length_2 = len(string_two)
    if abs(length_1 - length_2) > 1:
        return False
    max, min = (string_one, string_two) if length_1 > length_2 else (string_two, string_one)
    for i in range(len(max)):
        if i < len(min) and max[i] != min[i]:
            return max[i+1:] == min[i:]
    return True
'''
# Ignored replacement case above rip

def one_away(string_one, string_two):
    length_1 = len(string_one)
    length_2 = len(string_two)
    if length_1 == length_2:
        if string_one == string_two:
            return True
        for i in range(length_1):
            if string_one[i] != string_two[i] and i < length_1:
                return string_one[i+1:] == string_two[i+1:]
                # Time to reslice and then do compare - rip
    if abs(length_1 - length_2) > 1:
        return False
    max, min = (string_one, string_two) if length_1 > length_2 else (string_two, string_one)
    for i in range(len(max)):
        if i < len(min) and max[i] != min[i]:
            return max[i+1:] == min[i:]
    return True

def better_one_away(string_one, string_two):
    length_1 = len(string_one)
    length_2 = len(string_two)
    is_different = False
    # Case 1 - Strings are same length, replacement
    if length_1 == length_2:
        for i in range(length_1):
            if string_one[i] != string_two[i]:
                if is_different:
                    return False
                else:
                    is_different = True
        return True
    # Case 2 - Strings are different lengths
    # Bailout if difference is greater than 1, aka cannot simply insert/delete once
    if abs(length_1 - length_2) > 1:
        return False
    max, min = (string_one, string_two) if length_1 > length_2 else (string_two, string_one)
    max_i = 0
    min_i = 0
    while max_i < len(max) and min_i < len(min):
        if max[max_i] != min[min_i]:
            if is_different:
                return False
            else:
                is_different = True
                max_i += 1
        else:
            min_i += 1
            max_i += 1
    return True

# String slicing and comparison big O?
print(better_one_away(*test_1))
print(better_one_away(*test_2))
print(better_one_away(*test_3))
print(better_one_away(*test_4))
print(better_one_away(*test_5))
print(better_one_away(*test_6))
print(better_one_away(*test_7))
print(better_one_away(*test_8))



