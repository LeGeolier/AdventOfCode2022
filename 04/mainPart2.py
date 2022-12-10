def checkOverLaps(a,b,c,d):
    if ((a<c and b<c)or(c<a and d<a)):
        return False
    return True


def main():
    f = open('./04/ressource.txt')
    total = 0
    for line in f:
        leftPart = line.split(',')[0]
        rightPart = line.split(',')[1]

        leftLowerValue = int(leftPart.split('-')[0])
        leftHigherValue = int(leftPart.split('-')[1])

        rightLowerValue = int(rightPart.split('-')[0])
        rightHigherValue = int(rightPart.split('-')[1])
        boolOverlaps = checkOverLaps(leftLowerValue,leftHigherValue,rightLowerValue,rightHigherValue)
        if boolOverlaps:
            total +=1
    print(total)
    return



main()
