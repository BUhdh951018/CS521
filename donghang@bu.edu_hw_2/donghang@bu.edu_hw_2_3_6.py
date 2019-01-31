#Find the character of an ASCII code

asc = eval(input("Enter an ASCII code:"))

if asc < 0 or asc >127:
    print("Please enter a number between 0 and 127")
else :
    print(chr(asc))