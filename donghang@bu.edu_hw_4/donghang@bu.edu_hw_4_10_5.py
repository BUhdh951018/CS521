#Print distinct numbers

lst = []
s = input("Enter ten numbers:").split()
lst = [x for x in s]


lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
str = " ".join(lst2)
print("The distinct numbers are:", str)
