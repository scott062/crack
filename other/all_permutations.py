# all permutations
# return all sorted alpha perm of a given string
def all_permutations(word):
    my_list = []
    if len(word) == 1:
        return [word]
    for i in range(len(word)):
        l_side = word[:i]
        r_side = word[i+1:]
        copy = l_side + r_side
        letter = word[i]
        for x in all_permutations(copy):
            my_list.append(letter + x)
    return my_list

    
# c
# bc
# abc

print(all_permutations("abc"))



