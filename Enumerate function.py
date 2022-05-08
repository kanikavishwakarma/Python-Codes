# *********************************ENUMERATE FUNCTIONS**************************

list = ["bhindi","Aloo","gobi","brocolli"]

i=0
for item in list:
    if i%2 == 0:
        print( f"please buy {item}")
        #print("please buy",item)
    i=i+1

for i,item in enumerate(list):
    if i%2 == 0:
       print( f"please buy {item}")
