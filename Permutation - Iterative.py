# nPr = (n!) / (n-r)!
# nCr = n! / [ (r !) x (n – r)! ]

# ********************** ITERATIVE *********************

print("To find permutation")

def factorial(n):
     if n==1:
         return 1
     else:
         return n * factorial(n-1)


n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

p = factorial(n) / factorial(n-r)

print("Permutation : ",p)
