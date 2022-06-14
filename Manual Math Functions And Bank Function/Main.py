import numpy as np
import Bank as bk
import MyMath as mm

newBank = bk.BankAccount()

def Menu():
    print(f'''      **************** Welcome To Main Menu ****************
    
    Please select number of the following options.
    
    1.Math Functions
    2.BankAccount Functions
    ''')
    UserSelect()
def UserSelect():
    userInput = int(input("Your Choice is : "))
    if (userInput == 1):
        MenuMyMath()
    elif (userInput == 2):
        MenuBankAccount()
    else:
        print("Please enter only available numbers!")
        ChoiceAgain()

def ReturnToMainMenu():
    askLoop = input("Do you want to go back to Main Menu?(Y/N) : ")
    while True:
        if(askLoop in ['Y','y']):
                Menu()
                ReturnToMainMenu()
                break
        elif(askLoop in ['N','n']):
            print("**************** Thanks for using this program. ****************")
            break
        else:
            print("Your input format is incorrect!")
            print("Please correctly again!")
            ReturnToMainMenu()
            break

def ChoiceAgain():
    choiceAgain = input("Do you want to redo your Choice again?(Y/N) : ")
    while True:
        if (choiceAgain in ['Y', 'y']):
            UserSelect()
            ReturnToMenu()
            break
        elif (choiceAgain in ['N', 'n']):
            ReturnToMainMenu()
            print("**************** Thanks for using this program. ****************")
            break
        else:
            print("Please enter only available numbers!")
            print("Please correctly again!")
            ChoiceAgain()
            break

def MenuMyMath():
    print(f'''      **************** Welcome To Math Function Menu ****************
        
        Please select number of the following options.
        
        Note : You can add numbers as much as you want and please add space between numbers

        1.Addition
        2.Multiplication
        3.Exponential(**You can only enter two numbers in this function**)
        4.Searching Biggest Number
        5.Searching Smallest Number
        ''')
    UserSelect4MF()
    ReturnToMenu4MF()

def UserSelect4MF():
    userInput = int(input("Your Choice is : "))
    if (userInput == 1):
        mm.mySum()
    elif (userInput == 2):
        mm.myMul()
    elif (userInput == 3):
        myPowWithInput()
    elif (userInput == 4):
        mm.Max()
    elif (userInput == 5):
        mm.Min()
    else:
        print("Please enter only available numbers!")
        ChoiceAgain()

def ChoiceAgain4MF():
    choiceAgain = input("Do you want to redo your Choice again?(Y/N) : ")
    while True:
        if (choiceAgain in ['Y', 'y']):
            UserSelect()
            ReturnToMenu4MF()
            break
        elif (choiceAgain in ['N', 'n']):
            ReturnToMenu4MF()
            print("**************** Thanks for using this program. ****************")
            break
        else:
            print("Please enter only available numbers!")
            print("Please correctly again!")
            ChoiceAgain4MF()
            break

def ReturnToMenu4MF():
    askLoop = input("Do you want to go back to Math Function Menu?(Y/N) : ")
    while True:
        if(askLoop in ['Y','y']):
                MenuMyMath()
                break
        elif (askLoop in ['N','n']):
            ReturnToMainMenu()
            break
        else:
            print("Your input format is incorrect!")
            print("Please correctly again!")
            ReturnToMenu4MF()
            break

def myPowWithInput():
    userinput = list(
        input("Please Enter the numbers you want to do Calculation (Please space between numbers) : ").split())
    userinput = [int(j) for j in userinput]
    x = userinput[0]
    y = userinput[1]
    mm.myPow(x, y)

def MenuBankAccount():
    print(f'''      **************** Welcome To BankAccount Function Menu ****************

            Please select number of the following options.

            1.Deposit
            2.Withdraw
            3.Interest
            4.Balance
            ''')
    UserSelect4BA()
    ReturnToMenu4BA()

def UserSelect4BA():
    userInput = int(input("Your Choice is : "))
    if (userInput == 1):
        newBank.deposit()
    elif (userInput == 2):
        newBank.withdraw()
    elif (userInput == 3):
        newBank.interest()
    elif (userInput == 4):
        newBank.display()
    else:
        print("Please enter only available numbers!")
        ChoiceAgain4BA()

def ChoiceAgain4BA():
    choiceAgain = input("Do you want to redo your Choice again?(Y/N) : ")
    while True:
        if (choiceAgain in ['Y', 'y']):
            UserSelect()
            ReturnToMenu4BA()
            break
        elif (choiceAgain in ['N', 'n']):
            ReturnToMenu4BA()
            print("**************** Thanks for using this program. ****************")
            break
        else:
            print("Please enter only available numbers!")
            print("Please correctly again!")
            ChoiceAgain4BA()
            break

def ReturnToMenu4BA():
    askLoop = input("Do you want to go back to BankAccount Function Menu?(Y/N) : ")
    while True:
        if(askLoop in ['Y','y']):
            MenuBankAccount()
            break
        elif (askLoop in ['N','n']):
            ReturnToMainMenu()
            break
        else:
            print("Your input format is incorrect!")
            print("Please correctly again!")
            ReturnToMenu4BA()
            break

Menu()




