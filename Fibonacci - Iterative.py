# ************************* ITERATIVE APPROACH*******************************

print("To print fibonacci series")
# 0 1 1 2 3 5 8 13 21
print("Enter which term you want to print")
n = int(input())

a = 0
b = 1

if n==0:
    print("0")
elif n==1:
    print("0")  
elif n==2:
    print("1") 
else:
   
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        
print(n,"th term is",c)