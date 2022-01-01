def readFile():
    with open("../../../../Desktop/user.json") as file:
        data = file.read()
        print(data)
        print(type(data))


def writeIntoFile():
    with open("dummy.txt", mode='a') as file:
        file.write("\nNew data")


writeIntoFile()
readFile()
