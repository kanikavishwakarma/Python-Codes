#*************************** RECURSIVE APPROACH*******************************

print("To calculate factorial")
print("Enter any number: ")
n = int(input())

def fact(n):
    if n==1:
       return 1
    else:
       return n * fact(n-1)

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:   
   print("factorial of",n,"=",fact(n))
