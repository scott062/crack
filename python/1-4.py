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
    counts = [0] * 300
    copy_text = text.replace(" ", "")
    for x in copy_text: 
        counts[ord(x)] += 1
    odd_count = 0
    for count in counts:
        if count % 2 != 0:
            odd_count += 1
            if is_even(len(copy_text)) or odd_count > 1:
                return False
    return True
    
print(is_palindrome("231"))
