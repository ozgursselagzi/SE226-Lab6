import math

# First QUESTION
def firstFunction(n):

    double = lambda a: (float(n + 1) - 3) / math.pow(float(n + 1), 2)
    total = 0
    for i in range(n):
        total += double(n)
    return total

result = 1

# Second QUESTION
def secondFunction(n):
    global a

    a *= ((float(n) / (float(n) + 2)) - 10)

    if n > 1:
        secondFunction(n - 1)

number = int(input("Please enter a number :"))
print(firstFunction(number))

number = int(input("Please enter a second number :"))
secondFunction(number)
print(a)