def binary_search(items, target):
    if not items:
        return None

    half = len(items)//2
    current = items[half]
    if current == target:
        return half
    if len(items) == 1:
        return None
    if current > target:
        # Find left
        return binary_search(items[:half], target) 
    # Find right
    right = binary_search(items[half:], target)
    if right:
        return half + right 
    
    return None

# len = 5
# half = 2
# new half = 1

print(binary_search([1,2,3,4,5,10,11,12,13,14], 14))
print(binary_search([], 14))


