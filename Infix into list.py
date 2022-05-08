operator = ["+","-","*","/","%","^"]

numeral = ["0","1","2","3","4","5","6","7","8","9"]

expression = []

print("Enter the expression :")
exp = input()
print("Expression = ",exp)
operand = ""

for i in exp:
    # 22 + 32 - 1
    if i in numeral:
        operand = operand + i
    elif i in operator:
        expression.append(operand)
        expression.append(i)
        operand = ""
    else:
        print("Invalid character")
        break

expression.append(operand)
print("expression in from of list = ",expression)            





