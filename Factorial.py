#take input from user/keyboard
var = int(input("Enter a number: "));

def factorial(x):
    if x < 0:
        print("Your given number is negative !")
    elif x == 1:
        return 1
    else:
    	#recursion happens here 'factorial(x - 1)', function calls himself to find the value
        return x * factorial(x - 1);
        
print (factorial(var)); #calling the function for factorial
