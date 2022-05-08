# ************************* ITERATIVE APPROACH*******************************

print("To calculate factorial")
print("Enter any number: ")
n = int(input())

f = 1

for i in range(n):
    f = f + f*i

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:   
   print("factorial of",n,"=",f)