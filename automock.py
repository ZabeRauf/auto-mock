text = input("Enter text to convert\n")
textEnum = enumerate(text)
convertedText = ""

def convertToMock(input, output):
    for i in input:
        print(i)
        if(i[0] % 2 == 0):
            output += i[1].upper()
        else:
            output += i[1].lower()
    print(output)
        

convertToMock(textEnum, convertedText)

print(convertedText)