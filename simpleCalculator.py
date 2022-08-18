
#This is a calculator

n1 = int(input("Enter one digit: "))
op = input("Enter an operator: ")
n2 = int(input("Enter the other digit: "))

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    result = n1 / n2
else:
    result = "Invalid operator or parameters"

print(result)





