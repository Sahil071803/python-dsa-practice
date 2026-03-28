# 1) Develop a calender showing the year and month

# import calendar
#
# Year = int(input("Enter the year : "))
# Month = int(input("Enter the month : "))
#
# cal = calendar.month(Year, Month)
# print(cal)



# 2) The standard form of a quadratic equation is:
# where
# a, b and c are real numbers and
# The solutions of this quadratic equation is given by:
# 𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0
# 2
# 𝑎 ≠ 0
# (−𝑏 ± (𝑏 − 4𝑎𝑐 )/(2𝑎)

# import math
#
# a = float(input("Enter coefficient a : "))
# b = float(input("Enter coefficient b : "))
# c = float(input("Enter coefficient c : "))
#
# discriminant = (b ** 2) - (4 * a * c)
#
# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#
#     print(f"Root 1 : {root1}")
#     print(f"Root 2 : {root2}")
#
# elif discriminant == 0:
#     root = -b / (2 * a)
#     print(f"Root : {root}")
#
# else:
#     real_part = -b / (2 * a)
#     imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
#
#     print(f"Root 1 : {real_part} + {imaginary_part} i")
#     print(f"Root 2 : {real_part} - {imaginary_part} i")


# 3) Write a Python Program to Print the Fibonacci sequence.
# Fibonacci sequence:
# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
# the next number is obtained by adding the previous two numbers. This pattern continues
# indefinitely, generating a sequence that looks like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# Mathematically, the Fibonacci sequence can be defined using the following recurrence
# relation:
# 𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1

nterms = int(input("How many terms? " ))

n1,n2 = 0,1
count = 0

if nterms <= 0:
    print("Please enter a Positive Integer ")

elif nterms == 1:
    print("Fbionacci sequence upto" , nterms, " :")
    print(n1)

else :
    print("Fbionacci sequence : ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1




