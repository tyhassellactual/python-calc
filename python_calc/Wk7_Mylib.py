'''
Name: Tyler Hassell
Class: ENTD220 (Jan/Feb 2025)
Instructor: Sammy Abaza
Assignment: Week 7
Due date: 23Feb2025
Program name: Wk7_tyler_hassell.py
Library name: wk7_tyler_hassell_Mylib.py
'''


class allMath:
    
    #Class for all mathematical functions

    def checkNum(self, lr, num, hr):
        #Check if number is within a range
        return lr <= num <= hr

    def add(self, num1, num2):
        #Addition function
        return num1 + num2

    def sub(self, num1, num2):
        #Subtraction function
        return num1 - num2

    def mult(self, num1, num2):
        #Multiplication function
        return num1 * num2

    def div(self, num1, num2):
        #Division function
        try:
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2
        except ZeroDivisionError:
            return

    def allInOne(self, num1, num2):
        #All math functions that return a dictionary
        results = {
            "Addition": self.add(num1, num2),
            "Subtraction": self.sub(num1, num2),
            "Multiplication": self.mult(num1, num2)
        }
        try:
            results["Division"] = self.div(num1, num2)
        except ZeroDivisionError as e:
            results["Division"] = str(e)
        return results

    def scalc(self, p1):
        #Specialty calculator function
        star = p1.split(",")
        if len(star) != 3:
            raise ValueError
        try:
            num1 = float(star[0])
            num2 = float(star[1])
            operator = star[2].strip()

            if operator == "+":
                return self.add(num1, num2)
            elif operator == "-":
                return self.sub(num1, num2)
            elif operator == "*":
                return self.mult(num1, num2)
            elif operator == "/":
                return self.div(num1, num2)
            else:
                raise ValueError
        except ValueError:
            return

    

    
