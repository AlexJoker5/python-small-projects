
def userInput():
    userinput = list(
        input("Please Enter the numbers you want to do Calculation (Please space between numbers) : ").split())
    userinput = [int(j) for j in userinput]
    return userinput
def mySum():
    userinput = userInput()
    i = result = 0
    while (i <= len(userinput) - 1):
        result += userinput[i]
        i += 1

    print("Total sum is {}".format(result))


def myMul():
    userinput = userInput()
    i =0; result = 1
    while (i <= len(userinput) - 1):
        result *= userinput[i]
        i += 1
    print("Total multiplication is {}".format(result))


def myPow(x,y):
    print("Power value is {}".format(x**y))
def myMax():
    userinput = userInput()
    for i in range(1,len(userinput)):
        key = userinput[i]
        j = i - 1
        while j>=0 and key < userinput[j]:
            userinput[j + 1] = userinput[j]
            j -= 1
        userinput[j + 1] = key
        arrLen = len(userinput) - 1
        maxNum = userinput[arrLen]
    print(maxNum)

def myMin():
    userinput = userInput()
    for i in range(1, len(userinput)):
        key = userinput[i]
        j = i - 1
        while j >= 0 and key < userinput[j]:
            userinput[j + 1] = userinput[j]
            j -= 1
        userinput[j + 1] = key
        arrLen = len(userinput) - 1
        minNum = userinput[0]
    print(minNum)
