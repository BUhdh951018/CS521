#Find the number of years and days

minute = eval(input("Enter the number of minutes:"))

temp = 365 * 24 * 60
year = minute // temp
temp1 = minute % temp
day = temp1 // (24 * 60)
print(minute, "minutes is approximately", year, "years and", day, "days")