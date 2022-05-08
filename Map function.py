# ******************************** MAP FUNCTION **********************************

numbers = ["2","3","5","6","76","3","3","2"]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])
    
numbers = list(map(int,numbers))
numbers[2] = numbers[2] + 1
print(numbers[2]) 

def sq(a):
    return a*a

square= list(map(sq,numbers))
print(square)

sq= list(map(lambda x:x*x,numbers))
print(sq)

def square(a):
    return a*a

def cube(a):
    return a*a*a

function= [square,cube]

for i in range(5):
    val = list(map(lambda x:x(i),function))
    print(val)