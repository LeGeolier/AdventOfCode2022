
def main():
    f = open('./03/ressource.txt','r')
    alphabetValue ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    listElement1 =[]
    listElement2 = []
    for line in f:
        listElement1.append(line[0:int(((len(line))/2))])
        listElement2.append(line[int((len(line))/2):len(line)-1])
    for i in range(len(listElement1)):
        character = getCommonLetter(listElement1[i],listElement2[i])
        total += (alphabetValue.index(character)+1)
    print(total)
    return

def getCommonLetter(list1,list2):
    for letter1 in list1:
        for letter2 in list2:
            if(letter1 == letter2):
                return letter1

main()
