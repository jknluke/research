#these are the codes assigning each word to a proccess
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
#this is for when you are to run the the code display the question on what you would like to calculate
print("select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.didvde")
#this is when you are to enter your first and second number into the console 
while True:
    choice = input("Enter Choice (1/2/3/4: )")
    
    if choice in ("1,", "2", "3", "4"):
        num1 = float(input("Enter First Number: "))

        num2 = float(input("Enter Second Number: "))
#this is the calculator showing to add, sub, mult, or div your first and second number 
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == "1":
            print(num1, "+", num2, "=", subtract(num1, num2))

            break
        else:
            print("Invalid Input")
#Invalid input would show when there is a input that is not intended for this code

