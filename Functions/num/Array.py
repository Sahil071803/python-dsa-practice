
# from array import *

# val = array('i', [10,20,30,40,50])

# for i in range(len(val)):
#     print(val[i], end= " ")

from array import array

def array_example(val = array('i', [1,2,3,4,5,6,7])):
    result = []
    for i in range(len(val)):
        result.append(val[i])
        print(val[i], end=" ")
    return result

array_example()
