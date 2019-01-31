#Financial application: monetary units

money = eval(input("Enter an amount:"))

dollars = money // 100
cents = money % 100
print(dollars, "dollars", cents, "cents")