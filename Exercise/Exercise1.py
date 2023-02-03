listOfNumber = [16, 7, 412, -5]

biggestNumber = listOfNumber[0]
for currentNumber in listOfNumber:
    if biggestNumber < currentNumber:
        biggestNumber = currentNumber

print("The largest number is:", biggestNumber)