
from array import array

def multi_dim_arr(
    val = array('i', [
        1,5,9,
        3,5,7,
        4,8,6
    ])

):

    rows = 3
    col = 3

    result = []
    for i in range(rows):
        row = []
        for j in range(col):
            index = i * col + j
            row.append(val[index])
            result.append(val[index])
            print(val[index], end= " ")
        row.append(row)
        print()
    return result



multi_dim_arr()