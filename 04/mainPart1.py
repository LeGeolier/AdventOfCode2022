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
        if(leftLowerValue >= rightLowerValue and leftHigherValue <= rightHigherValue):
            total+=1
        elif(rightLowerValue >= leftLowerValue and rightHigherValue <= leftHigherValue):
            total+=1

    print(total)
    return

main()