



def count_num(text):
    text_copy = text.split(" ")
    sum = 0
    for phrase in text_copy:
        punc = "'.,!?;:`"
        p = phrase.rstrip(punc)
        if p.isnumeric():
            sum += int(p)
    return sum

text_1 = "1 2 3 one two three"
text_2 = "10 20 30 one two three 1st 22nd"

print(count_num(text_1)) # 6
print(count_num(text_2)) # 60

def count_num_opt(text):
    sum = 0
    i = 0 # index
    j = 0 # 2nd counter
    while i < len(text) and j < len(text): 
        if text[j] == " ": 
            punc = "'.,!?;:`"
            t = text[i:j].rstrip(punc)
            if t.isnumeric():
                sum += int(t)
            i = j + 1
            j = i 
        j += 1
    return sum

print(count_num_opt(text_1)) # 6
print(count_num_opt(text_2)) # 60
