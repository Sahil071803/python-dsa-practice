def even_odd(arr):
    even = []
    odd = []

    for num in arr:
        if num % 2 == 0:
            even.append(num)

        else:
            odd.append(num)

    return even, odd

arr = [1, 2, 3, 4, 5 , 6]
even, odd = even_odd(arr)

print("Even:", even)
print("Odd:", odd)
















