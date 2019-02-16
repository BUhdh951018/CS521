# Assign grades


def getScores():
    endOfInput = False
    while not endOfInput:
        number = input("Enter scores(end with 0):").split()
        score = [eval(i) for i in number]

        for i in score:
            if i == 0:
                endOfInput = True

    best = max(score)

    j = 0
    for element in score:
        if element == 0:
            break
        level = getGrade(element, best)
        print("Student {0:d} score is {1:d} and grade is {2}".format(j, score[j], level))
        j += 1


def getGrade(score, best):

    if score >= best - 10:
        return 'A'
    elif score >= best - 20:
        return 'B'
    elif score >= best - 30:
        return 'C'
    elif score >= best - 40:
        return 'D'
    else:
        return 'F'


getScores()

