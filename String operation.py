#  ************************ SLICING ***************************

a = "My name is kanika vishwakarma"
x = a[9:15]
print(x) 
y = a[:7]
print(y)
z = a[8:]
print(z)
print()


#  *********************** SPLITING ***************************

x = a.split(" ")
print(x)
x = a.split("a")
print(x)
print()

#  ********************* CONCATENATION ************************

b = "I am great"
print(a + " " + b)
print()

#  ********************* MULTIPLICATION ***********************

c = "kanika "
mul = 5 * c 
print(mul)
print()


star="*"
p=1*star
q=2*star
r=3*star
print(p+"\n"+q+"\n"+r)
print()


#  ****************** STAR PATTERN WITH LOOP *******************

num = int(input("Enter the no of lines : "))

for i in range(num+1):
    print(i* star)
    
