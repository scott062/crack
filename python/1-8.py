# Zero Matrix

def zero_matrix(matrix):
    rows = set()
    columns = set()
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if row[j] == 0:
                rows.add(i)
                columns.add(j)
    if rows or columns:
        for i in range(len(matrix)):
            row = matrix[i]
            if i in rows:
                matrix[i] = [0] * len(row)
                continue
            for j in range(len(row)):
                if j in columns:
                    row[j] = 0
    return matrix

a = [[1,2],[3,4],[0,5]]
b = [[1,2,3,4],[5,0,7,8]]
c = [[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

print(zero_matrix(c))

