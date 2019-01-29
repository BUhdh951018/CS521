# Display a pattern

counter = 5
while counter > 0:
    if counter == 5 or counter == 3:
        print("FFFFFFF")
    else:
        print("FF")
    counter -= 1

counter1 = 5
while counter1 > 0:
    if counter1 == 5 or counter1 == 4 or counter1 == 3:
        print("U     U")
    elif counter1 == 2:
        print(" U   U")
    else:
        print("  UUU")
    counter1 -= 1

print("NN    NN")
print("NNN   NN")
print("NN N  NN")
print("NN  N NN")
print("NN   NNN")