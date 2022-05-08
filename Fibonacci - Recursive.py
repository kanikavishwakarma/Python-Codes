#*************************** RECURSIVE APPROACH*******************************

print("To print fibonacci series")
# 0 1 1 2 3 5 8 13 21
print("Enter which term you want to print")
n = int(input())

def fibbo(n):
    if n == 0:
        return 0
    elif n==1:
        return 0   
    elif n==2:
        return 1
    elif n<0:
        print("Invalid input")
    else:
        return fibbo(n-1)+fibbo(n-2)
        
print(n,"th term is",fibbo(n))               
     

    
