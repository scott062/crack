def sparse_arrays(strings, queries):
    counter = []
    for q in queries:
        count = 0
        for s in strings:
            if s == q:
                count += 1
        counter.append(count)
    return counter


print(sparse_arrays(["a", "bc", "def", "a"], ["a", "b", "bc"]))

