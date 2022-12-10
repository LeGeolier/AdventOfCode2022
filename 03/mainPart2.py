
def main():
    f = open('./03/ressource.txt','r')
    alphabetValue ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total=0
    count = 0
    listLine1=[]
    listLine2 = []
    listLine3 = []
    for line in f:
        count+=1
        if count == 1:
            listLine1.append(line)
        elif count == 2:
            listLine2.append(line)
        else:
            listLine3.append(line)
            count = 0
    print("Length List 1 : {}\nLength List 2 : {}\nLength List 3 : {}".format(len(listLine1),len(listLine2),len(listLine3)))
    for i in range(len(listLine1)):
        character = getCommonLetter(listLine1[i],listLine2[i],listLine3[i])
        total += (alphabetValue.index(character)+1)
    print(total)
    return

def getCommonLetter(list1,list2,list3):
    for letter1 in list1:
        for letter2 in list2:
            for letter3 in list3:
                if(letter1 == letter2 and letter1==letter3):
                    return letter1

main()
