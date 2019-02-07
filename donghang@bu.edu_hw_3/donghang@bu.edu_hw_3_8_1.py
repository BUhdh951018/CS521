#Check SSN


def checkSSN():
    temp = 0

    while not temp:

        ssn = str(input("Enter a Social Security Number in the format ddd-dd-dddd:").strip())
        ssn1 = ssn.replace("-", "")
        if len(ssn1) != 9:
            print("Invalid SSN")
        else:
            if isValid(ssn):
                print("Valid SSN")
            else:
                print("Invalid SSN")


def isValid(ssn):
    return ssn[1:3].isdigit() and ssn[5:6].isdigit() and ssn[8:10].isdigit()

checkSSN()