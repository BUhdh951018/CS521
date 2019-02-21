# Palindrome integer


# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):
    n = list(number)
    n.reverse()
    return "".join(n)


# Return true id number is a palindrome
def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False


def main():

    number = input("Please enter a integer:")
    if isPalindrome(number):
        print("{0:d} is a palindrome number".format(int(number)))
    else:
        print("{0:d} is not a palindrome number".format(int(number)))


main()