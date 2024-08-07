def diag_diff(square_matrix):
    l_sum = 0
    r_sum = 0
    for i in range(len(square_matrix)):
        l_sum += square_matrix[i][i]
        r_sum += square_matrix[i][-1 - i]
    return abs(l_sum - r_sum)

print(diag_diff(
    [
        [1,1,0], 
        [1,2,0],
        [10,2,0]
    ]))
