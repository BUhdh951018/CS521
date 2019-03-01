# Process scores in a text file

name = input("Enter a filename:")
file = open(name, "r")
content = file.read().split()
print("There are", len(content), "numbers")
scores = [eval(x) for x in content]
total = sum(scores)
average = total / len(content)
print("The total is", total)
print("The average is", format(average, ".2f"))
file.close()

