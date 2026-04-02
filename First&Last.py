def first_last_same(arr):

    if len(arr) == 0:
        return False

    return arr[0] == arr[-1]

print(first_last_same([10, 20, 30, 10]))
print(first_last_same([1, 2, 3]))
print(first_last_same([]))