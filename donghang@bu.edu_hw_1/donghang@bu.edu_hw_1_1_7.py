#Approximate pi

s = -1
sum = 0
temp = 1
i = 0
while i < 8:
    s = s * (-1)
    temp = temp * s
    sum += temp
    if i == 5:
        print(sum*4)
    i += 1
    temp = 1 / (2 * i + 1)

print(sum*4)
