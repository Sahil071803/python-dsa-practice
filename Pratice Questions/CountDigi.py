
# Count the Digits 

# n = 5438
# num = n
# count = 0

# while num > 0:

#     count += 1
#     num = num // 10
    
# print("The number of digts in a number is:",count)

# def count_digits(n):

#     num = n
#     count = 0

#     while num > 0:
#         count += 1
#         num = num // 10

#     return count

# print(count_digits(5438))


    # n = 5438
    # if n == 0:
    #     return 1

    #     count = 0
    #     while n > 0:
    #         count += 1
    #         n = n // 10
    #     return count

# print(count_digits(0))


def count_digits(n):
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(0))