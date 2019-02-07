#Count positive and negative numbers and compute the averafe of numbers

number = eval(input("Enter an integer, the input ends if it is 0:"))

positive = 0
negative = 0
total = 0
sum = 0

if number != 0:
    total = 1
    sum = number
    if number > 0:
        positive += 1
    else:
        negative += 1

    while number != 0:
        number = eval(input("Enter an integer, the input ends if it is 0:"))
        if number == 0:
            break
        else:
            if number > 0:
                positive += 1
            else:
                negative += 1
            total += 1
        sum = sum + number

    average = sum / total
    print("The number of positives is", positive, "\n", "The number of negatives is", negative)
    print("The total is", total + 1)
    print("The average is", average)

else:
    print("You didn't enter any number")