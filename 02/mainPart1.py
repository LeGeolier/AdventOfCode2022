'''
Here we will as before read a file text line by line 
for each line we will make some few verification 
and then 
add the result of the match to a total

A => Rock
B => Paper
C => Scissors

X => Rock
Y => Paper
Z => Scissors
'''
def main():
    f = open('./02/ressource.txt','r')
    totalPts = 0
    for line in f:
        yourChoice = line[2]
        enemyChoice = line[0]
        # Points earned by the shape selection
        if yourChoice== "X":
            totalPts += 1
        elif yourChoice == "Y":
            totalPts += 2
        else:
            totalPts += 3
        # Points earned by a win
        if ((yourChoice == "X" and enemyChoice == "C") or (yourChoice == "Y" and enemyChoice =="A") or (yourChoice =="Z" and enemyChoice =="B")): 
            totalPts += 6
        # Points earned by a draw 
        elif ((yourChoice == "X" and enemyChoice == "A") or (yourChoice == "Y" and enemyChoice =="B") or (yourChoice =="Z" and enemyChoice =="C")):
            totalPts += 3
    print(totalPts)
    return

main()