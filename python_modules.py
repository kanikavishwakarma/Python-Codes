# import math

# x=4
# y=math.sqrt(x)
# print(x)
# print(y)


# import math as m

# print("importing module using as")
# x=4
# y= m.sqrt(x)
# print("value of x =",x)
# print("value of y =",y)


# from math import sqrt

# print("importing module using from")
# x=5
# y=sqrt(x)
# print("value of x =",x,"\nvalue of y =",y)


# from math import *

# print("By using * we don't need to write math.")
# x=5
# y=sqrt(x)
# print("value of x =",x,"\nvalue of y =",y)


# USING TIME MODULE

import time

initial= time.time()
print("time before for loop =",initial)

for i in range(5):
    print(i)
    time.sleep(1)

final= time.time()
print("time after for loop =",final)

print("For loop ran in",final-initial,"time")

localtime = time.asctime()
print("\nLocaltime =",localtime)


# import sys
# print(sys.path)


# WE CAN ALSO IMPORT OUR OWN FILE AND USE ITS FUNCTIONS

# import file2
# print(file2.a)
# file2.printjoke("hahahaha!")

# from file2 import a
# print(a)



