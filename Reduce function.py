# ******************************** REDUCE FUNCTION **********************************    


from functools import reduce


list = [1,2,3,4,5]

num = reduce(lambda x,y:x+y,list)
print(num)
