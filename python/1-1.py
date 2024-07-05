import pytest

'''
Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

# TO DO: Practice more efficient bit manipulation approach

# ----------------------------------------------------------------------------


# Strategy with counter

# Define a counter
# Loop on input, counting each char
# Check count if any > 1

def is_unique(input_string: str) -> bool:
    if not input_string:
        raise ValueError("input_string must be string")
    else:
        max_uniq_char = 300 # Aha moment - can only be so many unique character per ascii or unicode
        if len(input_string) > max_uniq_char:
            return False

        counter = {}
        for char in input_string:
            if counter.get(char):
                return False
            else:
                counter[char] = 1
        return True

# Worst case run time is O(N), N being length of input string
# However using the optimization for max_unique_char we improve this to O(1)
# Worst case memory is O(1), N being max possible length of input string to build counter dict


# ----------------------------------------------------------------------------


# Strategy with python magic

# Define a copied set
# Compare length of set to len of input

def is_unique_python(input_string: str) -> bool:
    if not input_string:
        raise ValueError("input_string must be string")
    else:
        max_uniq_char = 300
        if len(input_string) > max_uniq_char:
            return False
        return len(set(input_string)) == len(input_string)

# Worst case run time is O(N), N being length of input string
# However using the optimization for max_ unique_ char we convert this to O(1)
# Worst case memory is O(1), N being max possible length of input string to build counter dict


# ----------------------------------------------------------------------------


# Strategy without additional data structures

# Loop on input 
# Check char
# Loop on the remainder of the input_string to see if any char matches current

def is_unique_no_counter(input_string: str) -> bool:
    if not input_string:
        raise ValueError("input_string must be string")
    else:
        max_uniq_char = 300
        if len(input_string) > max_uniq_char:
            return False
        for idx in range(len(input_string)):
            if idx < (len(input_string) - 2):
                for other_char in input_string[idx + 1:]:
                    if input_string[idx] == other_char:
                        return False
        return True

# Worst case run time is O(N**2), N being length of input string
# Worst case memory is O(1)
# Sacrifices run time for memory


# ----------------------------------------------------------------------------


# Strategy without additional data structures (again)

# Sort input_string in place
# Loop on input 
# Check next char

def is_unique_no_counter_sort(input_string: str) -> bool:
    if not input_string:
        raise ValueError("input_string must be string")
    else:
        max_uniq_char = 300
        if len(input_string) > max_uniq_char:
            return False
        input_string = sorted(input_string)
        for idx in range(len(input_string)):
            if idx < (len(input_string) - 2):
                if input_string[idx] == input_string[idx + 1]:
                    return False
        return True

# Run time is O(N LOG(N)), as it has to be sorted 
# Worst case memory is O(1)
# Sacrifices run time for memory


# ----------------------------------------------------------------------------

TESTS = [
    ("abcdefg", True),
    ("aAcCeEg", True),
    ("a!1e{}*/", True),
    ("aaaaaaa", False),
    ("*******", False),
    ("abcdAABBCCabcd", False),
    ("**++=={", False),
    ("", False),
]

class TestIsUnique:
    def test_unique_lowercase_letters(self):
        t = TESTS[0]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_lowercase_uppercase_letters(self):
        t = TESTS[1]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_symbols_letters(self):
        t = TESTS[2]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_letters(self):
        t = TESTS[3]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_symbols(self):
        t = TESTS[4]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_uppercase_letters(self):
        t = TESTS[5]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_multi_same_symbols(self):
        t = TESTS[6]
        assert is_unique(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_exception(self):
        t = TESTS[7]
        with pytest.raises(ValueError):
            is_unique(t[0])

class TestIsUniquePython:
    def test_unique_lowercase_letters(self):
        t = TESTS[0]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_lowercase_uppercase_letters(self):
        t = TESTS[1]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_symbols_letters(self):
        t = TESTS[2]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_letters(self):
        t = TESTS[3]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_symbols(self):
        t = TESTS[4]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_uppercase_letters(self):
        t = TESTS[5]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_multi_same_symbols(self):
        t = TESTS[6]
        assert is_unique_python(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_exception(self):
        t = TESTS[7]
        with pytest.raises(ValueError):
            is_unique_python(t[0])

class TestIsUniqueNoCounter:
    def test_unique_lowercase_letters(self):
        t = TESTS[0]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_lowercase_uppercase_letters(self):
        t = TESTS[1]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_symbols_letters(self):
        t = TESTS[2]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_letters(self):
        t = TESTS[3]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_symbols(self):
        t = TESTS[4]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_uppercase_letters(self):
        t = TESTS[5]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_multi_same_symbols(self):
        t = TESTS[6]
        assert is_unique_no_counter(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_exception(self):
        t = TESTS[7]
        with pytest.raises(ValueError):
            is_unique_no_counter(t[0])


class TestIsUniqueNoCounterSort:
    def test_unique_lowercase_letters(self):
        t = TESTS[0]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_lowercase_uppercase_letters(self):
        t = TESTS[1]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_unique_symbols_letters(self):
        t = TESTS[2]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_letters(self):
        t = TESTS[3]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_symbols(self):
        t = TESTS[4]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_same_lowercase_uppercase_letters(self):
        t = TESTS[5]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_multi_same_symbols(self):
        t = TESTS[6]
        assert is_unique_no_counter_sort(t[0]) is t[1], f"Expected is_unique({t[0]}) to return {t[1]}"

    def test_exception(self):
        t = TESTS[7]
        with pytest.raises(ValueError):
            is_unique_no_counter_sort(t[0])

