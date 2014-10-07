var = int(input("Enter a number: "));

def factorial(x):
    if x < 0:
        print("Your given number is negative !")
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1);
        
print (factorial(var));
