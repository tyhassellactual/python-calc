# import math functions
import Wk7_Mylib as tjh
#import custom exceptions
import myExceptions_lib as htj

# create object to inherit the library functions
allCalc = tjh.allMath()

def getRange():
    while True:
        # get lower and upper range
        try:
            lowerRange = float(input("Enter lowest number in range: "))
            upperRange = float(input("Enter the highest number in range: "))
            # check for proper lowerRange v. upperRange
            if lowerRange >= upperRange:
                print("Lower range must be less than upper range")
                continue
            return lowerRange, upperRange
        except ValueError:
            print("Please enter valid numbers")

def getNumbers(lowRange, upperRange):
    while True:
        # get two numbers and check if within range
        try:
            num1 = float(input("Enter your first number: "))
            if not allCalc.checkNum(lowRange, num1, upperRange):
                print(f"{num1} is not between {lowRange} and {upperRange}")
                continue
                
            num2 = float(input("Enter your second number: "))
            if not allCalc.checkNum(lowRange, num2, upperRange):
                print(f"{num2} is not between {lowRange} and {upperRange}")
                continue
                
            return num1, num2
        except ValueError:
            print("Please enter valid numbers")

def displayMenu():
    # display the working menu for the user
    menu = [
        "1) Add two numbers", # allCalc.add(num1, num2)
        "2) Subtract two numbers", # allCalc.sub(num1, num2)
        "3) Multiply two numbers", # allCalc.mult(num1, num2)
        "4) Divide two numbers", # allCalc.div(num1, num2)
        "5) Perform all of the above", # allCalc.allInOne(num1, num2)
        "6) Choose 2 numbers and operator", # must get input for allCalc.scalc(p1)
        "7) Exit" # exit program
    ]

    print("\nWithin a range of numbers...")
    print("Calculator Menu:")
    for item in menu:
        print(item)

def main():
    while True:
        try:
            # get user choice
            displayMenu()
            choice = input("Enter your choice 1-7: ")
            # exit program
            if choice == '7':
                print("Thanks for using my program")
                break
            # add, sub, mult, div, allInOne choice    
            if choice in ['1', '2', '3', '4', '5']:
                lowRange, upperRange = getRange()
                num1, num2 = getNumbers(lowRange, upperRange)
                
                if choice == '1':
                    result = allCalc.add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = allCalc.sub(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = allCalc.mult(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = allCalc.div(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = allCalc.allInOne(num1, num2)
                    #print(result) #returns straight dictionary
                    print("\nAll operations results:")
                    print(f"{num1} + {num2} = {result['Addition']}")
                    print(f"{num1} - {num2} = {result['Subtraction']}")
                    print(f"{num1} * {num2} = {result['Multiplication']}")
                    print(f"{num1} / {num2} = {result['Division']}")
            # scalc choice    
            elif choice == '6':
                p1 = input("Enter two numbers and operator (format: num1, num2, operator): ")
                result = allCalc.scalc(p1)
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please select 1-7")
            # Continue?
            more = input("\nWould you like to do more calculations? Y/N: ").strip().upper()
            if more == "Y":
                continue
            elif more == "N":
                print("Thanks for using my program")
                break
            else:
                raise htj.makeGoodChoices
                
        except htj.makeGoodChoices:
            print("\nYou did not enter 'Y' or 'N'")
            continue

# begin program
main()