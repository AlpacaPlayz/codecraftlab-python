def add(num1, num2):
    final = num1 + num2
    return final
def sub(num1, num2):
    final = num1 - num2
    return final
def multiply(num1, num2):
    final = num1 * num2
    return final
def divide(num1, num2) :
    final = num1 / num2
    return final

print("What are your numbers?")
n1 = int(input())
n2 = int(input())
print("What funtion do you want to use?")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")


answer=input ()
if answer == "addition":
    print(add(n1, n2))
elif answer == "subtraction":
    print(sub(n1, n2))
elif answer == "multiplication":
    print(multiply(n1, n2))
elif answer == "division":
    print(divide(n1, n2))

