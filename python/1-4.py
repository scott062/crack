# Palindrome Permutation
# taco cat => t a c o c a t
# taco cat => a c t o t c a
# abbbba => a b b b a 
# Can a palindrome have an even number of letters?
'''
def is_palindrome(text):
    count = [0] * 300
    copy_text = text.replace(" ", "")
    len_text = len(copy_text)
    for x in copy_text: 
        count[ord(x)] += 1
    # Even
    if len_text % 2 == 0:
        print("is even")
        for x in count:
            if x % 2 != 0:
                return False
        return True
    # Odd
    else:
        print("is odd")
        odd_count = 0
        for x in count:
            if x % 2 != 0:
                if odd_count > 0:
                    return False
                else:
                    odd_count = 1
        return True
'''
        
def is_even(num):
    return num % 2 == 0


def is_palindrome(text):
    counts = [0] * 300 # Max number of unique chars or letters depending on how you read the question
    oddcount = 0
    for x in text: 
        if x != " ":
            counts[ord(x)] += 1
            # Check current char count and set odd count ind
            if is_even(counts[ord(x)]):
                oddcount -= 1
            else:
                oddcount += 1
    return oddcount <= 1
    
def is_palindrome_set(text):
    counts = set()
    for char in text:
        if char != ' ':
            if char in counts: # Not sure if set lookups for 'in' are O(1)
                counts.remove(char)
            else:
                counts.add(char)
    return len(counts) <= 1


print(is_palindrome("121"))
