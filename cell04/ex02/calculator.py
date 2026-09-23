number1 = int(input("Give me the first number : "))
number2 = int(input("Give me the second number : "))

print("Thank you!")

for operator in ["+", "-", "/", "*"] :
    if operator == "+" :
        result = number1 + number2
    elif operator == "-" :
        result = number1 - number2
    elif operator == "/" :
        result = int(number1 / number2)
    else :
        result = number1 * number2
        
    print(number1, operator, number2, "=", result)