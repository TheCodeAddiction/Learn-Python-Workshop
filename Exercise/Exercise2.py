listOfNumber = [16, 7, 412, -5]
new_list = []

while listOfNumber:
    smallestNumber = listOfNumber[0]
    for number in listOfNumber:
        if number < smallestNumber:
            smallestNumber = number
    new_list.append(smallestNumber)
    listOfNumber.remove(smallestNumber)

print(new_list)