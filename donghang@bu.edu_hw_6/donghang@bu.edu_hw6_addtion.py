def count_alphabetical(list, dic):
    dic = dic
    frequency = []
    for x in dic:
        temp = list.count(x)
        frequency.append(temp)
    return frequency


def main():
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    name = input("Enter a filename(test.txt):")
    file = open(name, "r")
    content = file.read()
    str = content.lower()
    freq = count_alphabetical(str, dic)
    sum = 0
    for i in freq:
        sum += i
    print("Char  Freq   total(%)")
    for j in range(0, 26):
        print("{0:5} {1:<4} {2:6.2f}".format(dic[j], freq[j], freq[j] / sum * 100))


if __name__ == '__main__':
    main()
