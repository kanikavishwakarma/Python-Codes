
# nPr = (n!) / (n-r)!
# nCr = n! / [ (r !) x (n – r)! ]

# ********************** RECURSIVE *********************

print("To find permutation")

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

def factorial(n):
     if n == 1:
         return 1
     else:
         return n * factorial(n-1)

temp = n
n = factorial(n)
r = factorial(temp-r)

print("Permutation : ", n/r)
        
            




