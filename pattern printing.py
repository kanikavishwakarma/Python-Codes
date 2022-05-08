print("Enter how many rows you want in your pyramid:")
n = int(input())

print("Enter 1 to print up triangle \nEnter 0 to print down triangle")
ch = int(input())

new = bool(ch)

if new == True:
       for i in range(0,n):
           for j in range(0,i+1):
               print("*",end=" ")
           print()       

elif new == False:
        for i in range(n,0,-1):
            for j in range(0,i):
                print("*",end=" ")
            print()    
            




