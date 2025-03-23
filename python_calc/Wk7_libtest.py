import Wk7_Mylib as tjh

allCalc = tjh.allMath()
para1 = 3
para2 = 0
para3 = 10
paras = "10, 5, *"

addResult = allCalc.add(para1, para2)
print(f"Addition Result: {addResult}")
subResult = allCalc.sub(para1, para2)
print(f"Subtraction Result: {subResult}")
mulResult = allCalc.mult(para1, para2)
print(f"Multiplication Result: {mulResult}")
divResult = allCalc.div(para1, para2)
print(f"Division Result: {divResult}")
checkResult = allCalc.checkNum(para1, para2, para3)
print(f"Check Number Result: {checkResult}")
scalcResult = allCalc.scalc(paras)
print(f"Specialty Calculator Result: {scalcResult}")
checkAllCalc = allCalc.allInOne(para1, para2)
print(f"allInOne Results: {checkAllCalc}")