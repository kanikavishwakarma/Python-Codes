# ******************************** FILTER FUNCTION **********************************    


no = [1,2,3,4,5,6,7,8,9]

def is_greater(num):
    return num>5

greater = list(filter(is_greater,no))
print(greater)   