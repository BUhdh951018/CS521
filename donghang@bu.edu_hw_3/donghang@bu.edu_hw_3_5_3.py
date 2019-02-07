#Conversion from kilograms to pounds

print("Kilograms", "\t", "Pounds")
k = 1
for i in range(1, 101):

    p = 2.2 * k
    print("{0:<9} {1:>9.1f}".format(k, p))
    k += 2
