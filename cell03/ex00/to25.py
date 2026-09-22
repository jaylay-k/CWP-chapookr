number = int(input("Enter a number less than 25 : "))

if number < 25 :
    while(number < 25) :
        number += 1
        print("Inside the loop, my variable is",number)
else :
    print("Error")