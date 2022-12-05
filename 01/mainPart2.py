# Here for this we will mostly use the same structure as the part one but we're gonna use the pop method to fetch the top 3 elf.


def main():
    f = open("./01/ressource.txt","r")
    response = []
    value = 0
    for line in f:
        if len(line) == 1:
            response.append(value)
            value = 0
        else:
            value += int(line)
    sumOfThree = 0
    count = 0
    for i in range(3):
        sumOfThree += max(response)
        response.remove(max(response))
        count+=1
        print(count)
    print(sumOfThree)
    return


main()