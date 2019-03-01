# Use trigonometric functions
import math

print("Degree", "\t", "Sin", "\t\t", "Cos")

for i in range(0, 370, 10):
    print(format(i, "<3"), "\t", format(math.sin(math.radians(i)), ".4f"), "\t",
          format(math.cos(math.radians(i)), ".4f"), "\t")
