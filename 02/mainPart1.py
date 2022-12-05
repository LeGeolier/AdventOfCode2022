'''Here we will as before read a file text line by line 
for each line we will make some few verification 
and then 
add the result of the match to a total
'''
def main():
    f = open('./02/ressource.txt','r')
    totalPts = 0
    for line in f:
        print('First letter {} second letter {}'.format(line[0],line[2]))

    return

main()