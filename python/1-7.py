# Rotate Matrix
# [[a, b, c,],
#  [d, e, f,],
#  [g, h, i]]

def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        # Looping forwards
        new = []
        for j in range(len(matrix)):
            new.append(matrix[len(matrix) - 1 - j][i]) # Starting at the end and inserting in reverse
        new_matrix.append(new)
    return new_matrix

print(rotate_matrix([["a","b","c"],["d","e","f"],["h","i","j"],]))

def rotate_matrix_other(matrix):
    return [list(reversed(row)) for row in zip(*matrix)] # Way cooler way to do this - noting reversed and zip

print(rotate_matrix_other([["a","b","c"],["d","e","f"],["h","i","j"],]))

        

