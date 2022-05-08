print("Enter any year to check whether it's leap year or not!!")
year = int(input())

if (year%4 == 0 and year%100 != 0) | (year%400 == 0 and year%100 != 0):
    print(year,"is a leap year")

else:
       print(year,"is not a leap year")

