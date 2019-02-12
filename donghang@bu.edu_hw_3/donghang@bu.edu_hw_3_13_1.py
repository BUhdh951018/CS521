#Remove text


X_str = "It was the best of times, " \
        "it was the worst of times, " \
        "it was the age of wisdom, " \
        "it was the age of foolishness, " \
        "it was the epoch of belief, " \
        "it was the epoch of incredulity, " \
        "it was the season of Light, " \
        "it was the season of Darkness, " \
        "it was the spring of hope, " \
        "it was the winter of despair, " \
        "we had everything before us, " \
        "we had nothing before us, " \
        "we were all going direct to Heaven, " \
        "we were all going direct the other way – in short, " \
        "the period was so far like the present period, " \
        "that some of its noisiest authorities insisted on its being received, " \
        "for good or for evil, in the superlative degree of comparison only"
word = input("Enter a word to be removed:").strip()

new = X_str.replace(word, "").strip()
count = X_str.count(word)

print(new, "\n", "There are", count, "\"", word, "\" in the string")

number = 0

X_list = X_str.split()
j = len(X_list)
for i in range(j):

    if X_list[i] == word:
        for m in range(i, j-1):
            X_list[m] = X_list[m+1]
        number += 1

        for n in range(j-number, j):
            X_list[n] = ""
Y_str = " ".join(X_list)
print(Y_str, "\n", "There are", number, "\"", word, "\" in the string")

Y_list = X_str.split()
j = len(Y_list)
for i in range(4, j, 5):
    temp = list(Y_list[i])
    temp.reverse()
    re_str = "".join(temp)
    Y_list[i] = re_str
Y_str = " ".join(Y_list)
print(Y_str)
