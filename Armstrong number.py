# Consider the number 371.Number of digits in 371 is 3.So,

# 3*3*3 + 7*7*7 + 1*1*1 =371
# which is equal to the given number. Therefore, 371 is an armstrong number.

print("Enter the number = ")
n = int(input())

temp = n
sum = 0
mul = len(str(n))

while(temp != 0):
    rem = temp % 10
    sum = sum + rem ** mul
    temp = temp //10


if sum == n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")        
