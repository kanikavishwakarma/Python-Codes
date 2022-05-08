# ************************* METHOD 1 *************************

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

a = 45 
b = 89
print("Maximum of two numbers : ",maximum(a,b))


# ************************* METHOD 2 *************************


a= 67
b= 90
m = max(a,b)
print("Maximum of two numbers  : ",m)


# ************************* METHOD 3 *************************

a = 456
b = 333

print("Maximum of two numbers : ",a if a>=b else b)

