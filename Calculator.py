def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

ans = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = float(input("Enter the first number:"))
for symbol in ans:
    print(symbol)
operator = input("Pick an operator:")
second_number = float(input("Enter the second number:"))
result = (ans[operator](first_number, second_number))
print(result)

key = True
while key:
    hey = input("Do you want to continue working with previous result? (yes/no) ").lower()
    if hey == "yes":
        first_number = result
        for symbol in ans:
            print(symbol)
        operator = input("Pick an operator:")
        second_number = float(input("Enter the second number:"))
        result = (ans[operator](first_number, second_number))
        print(result)
    else:
        key = False
        print("Thank You..!!! For Using The Calculator..GoodByeee...!!!")