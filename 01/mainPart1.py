# This program should be able to :
#   1. Open a file and read it line by line
#   2. Sum all the value who aren't broken by two consecutive "\n"
#   3. Put the summed value into a list
#   4. When the whole file have been read we close it
#   5. Then we fetch the Maximum value of this list and it's index.

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
    print(max(response))
    return


main()