import myModule as md
import math

def Menu():
    print(f'''************** Welcome to Menu **************
    
    Please select number of the following converting functions as you wish.
    
    1.Converting Celsius into Fahrenheit.
    2.Converting Fahrenheit to Celsius.
    3.Converting Kilograms to pound.
    4.Converting Pound to kilograms.
    5.Converting Pound to Ounces.
    6.Converting Ounces to Pound.
    7.Converting Kilometers to miles.
    8.Converting Feet to inches.
    9.Converting Centimeters to meters.
    ''')



def ReturnToMenu():
    askLoop = input("Do you want to go back to Menu?(Y/N) : ")
    while True:
        if(askLoop in ['Y','y']):
                Menu()
                UserSelect()
                ReturnToMenu()
                break
        elif (askLoop in ['N','n']):
            print("**************** Thanks for using this converter. ****************")
            break
        else:
            print("Your input format is incorrect!")
            print("Please correctly again!")
            ReturnToMenu()
            break
def ChoiceAgain():
    choiceAgain = input("Do you want to redo your Choice again?(Y/N) : ")
    while True:
        if (choiceAgain in ['Y', 'y']):
            UserSelect()
            break
        elif (choiceAgain in ['N', 'n']):
            print("**************** Thanks for using this converter. ****************")
            break
        else:
            print("Please enter only available numbers!")
            print("Please correctly again!")
            ChoiceAgain()
            break

def UserSelect():
    userInput = int(input("Your Choice is : "))
    if (userInput == 1):
        cToFInput = int(input("Please enter temperature in Celsius : "))
        cToFOutput = float(md.cToF(cToFInput))
        print("Temperature in Fahrenheit : {} F".format(cToFOutput))
    elif (userInput == 2):
        fToCInput = float(input("Please enter temperature in Fahrenheit : "))
        fToCOutput = int(md.fToC(fToCInput))
        print("Temperature in Celsius : {} C".format(fToCOutput))
    elif (userInput == 3):
        kgToLbInput = float(input("Please enter weight in Kilograms : "))
        kgToLbOutput = round(md.kgToLb(kgToLbInput),2)
        print("Weight in Pound : {} lbs".format(kgToLbOutput))
    elif (userInput == 4):
        lbToKgInput = float(input("Please enter weight in Pound : "))
        lbToKgOutput = round(md.lbToKg(lbToKgInput),2)
        print("Weight in Kilograms : {} kg".format(lbToKgOutput))
    elif (userInput == 5):
        lbToOunceInput = float(input("Please enter weight in Pound : "))
        lbToOunceOutput = round(md.lbToOunce(lbToOunceInput),2)
        print("Weight in Ounce : {} oz".format(lbToOunceOutput))
    elif (userInput == 6):
        ounceToLbInput = float(input("Please enter weight in Ounce : "))
        ounceToLbOutput = round(md.ounceToLb(ounceToLbInput),2)
        print("Weight in Pound : {} lbs".format(ounceToLbOutput))
    elif (userInput == 7):
        kmToMileInput = float(input("Please enter distance in Kilometer : "))
        kmToMileOutput = round(md.kmToMile(kmToMileInput),2)
        print("Distance in Mile : {} mile".format(kmToMileOutput))
    elif (userInput == 8):
        ftToInchInput = float(input("Please enter height in Feet : "))
        ftToInchOutput = round(md.ftToInch(ftToInchInput),2)
        print("Height in Inch : {} inches".format(ftToInchOutput))
    elif (userInput == 9):
        cmToMInput = float(input("Please enter height in Centimeter : "))
        cmToMOutput = round(md.cmToM(cmToMInput),2)
        print("Height in Meter : {} m".format(cmToMOutput))
    else:
        print("Please enter only available numbers!")
        ChoiceAgain()

Menu()
UserSelect()
ReturnToMenu()








