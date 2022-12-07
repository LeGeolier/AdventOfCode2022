'''
Here we will as before read a file text line by line 
for each line we will make some few verification 
and then add the result of the match to a total

A => Rock
B => Paper
C => Scissors

X => Loose
Y => Draw
Z => Win
'''
def main():
    f = open('./02/ressource.txt','r')
    totalPts = 0
    for line in f:
        yourChoice = line[2]
        enemyChoice = line[0]
        # Points earned by the shape selection
        if yourChoice== "Z":
            totalPts += 6
        elif yourChoice == "Y":
            totalPts += 3
        # Points earned by copying Rock
        if((enemyChoice == "A" and yourChoice == "Y") or (enemyChoice == "B" and yourChoice == "X") or (enemyChoice == "C" and yourChoice =="Z")):
            totalPts += 1
        # Points earned by copying Paper
        elif((enemyChoice == "B" and yourChoice == "Y") or (enemyChoice == "C" and yourChoice == "X") or (enemyChoice == "A" and yourChoice =="Z")):
            totalPts +=2
        # Points earned by copying scissor
        else:
            totalPts +=3
    print(totalPts)
    return

main()