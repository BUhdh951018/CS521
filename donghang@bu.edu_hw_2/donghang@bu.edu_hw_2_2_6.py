#Sum the digits in an integer

integer = eval(input("Enter a number between 0 and 1000:"))

if integer == 1000:
    print("The sum of the digits is 1")
else:
    a = integer % 10
    temp = integer // 10
    b = temp % 10
    temp = temp // 10
    c = temp % 10
    sum = a + b + c

    print("The sum of the digits is", sum)