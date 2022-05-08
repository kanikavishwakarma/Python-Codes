# ******************************** JOIN FUNCTION *********************************


list = ["bhindi","Aloo","gobi","brocolli"]

for item in list:
    print(item,"and",end=" ")
print("other vegetables")



list = ["bhindi","Aloo","gobi","brocolli"]

a=" and ".join(list)
print(a," and other vegetables")

a= ",".join(list)
print(a,",other vevgetables")
