print("To check whether the given string is pallindrome or not")

print("Enter any string")
str = input()

rev = str[::-1]

if str == rev:
    print("It as a pallindrome")
else:
    print("It is not a pallindrome")
    
        