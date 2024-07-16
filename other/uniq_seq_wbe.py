# Examples
# [1,2,3,4] => [] 
# [1,2,3,4,4] => [4,4] 
# [1,1,1,1] => [1,1,1,1] 
# [1,2,1,3,2] => [1,2,1,2] 

def remove_unique(data):
    return [x for x in data if data.count(x) > 1]
    '''
    data_copy = data.copy()
    for num in data:
        if data.count(num) == 1:
            data_copy.remove(num)
    return data_copy
    '''
    '''    
    for idx in range(len(data)):
        if idx == len(data) - 1:
           if data[idx] in new_list:
                new_list.append(data[idx])
        elif data[idx] in data[idx + 1:] or data[idx] in new_list:
            new_list.append(data[idx])
    return new_list
       ''' 
    
all_uniq = [1, 2, 3, 4]
all_same = [1, 1, 1, 1]
some_same = [1,2,1,3,2] 

print(remove_unique(all_uniq)) # []
print(remove_unique(all_same)) # [1,1,1,1]
print(remove_unique(some_same)) # => [1,2,1,2] 

    
