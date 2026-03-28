
def is_armstrong(n):
    # n = 153
    num = n
    total = 0

    nod: int = len(str(num))

    while num > 0:
        ld = num % 10
        total = total + ld ** nod

        num = num // 10

    return total == n

print(is_armstrong(7744))