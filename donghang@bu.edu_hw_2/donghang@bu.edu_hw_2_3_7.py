#Random character
import time

a = time.time()
b = int(a % 26)
b = b + 65
c = chr(b)
print(c)