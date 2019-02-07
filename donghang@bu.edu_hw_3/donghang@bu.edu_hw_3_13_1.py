#Remove text

string = 1
while string != "":
    string = input("Enter a string:").strip()
    word = input("Enter a word to be removed:").strip()

    new = string.replace(word, "").strip()

    print(new)