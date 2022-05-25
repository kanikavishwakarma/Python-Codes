#Program to swap two elements in a lisr

def swapping(list,p1,p2):
    list[p1],list[p2]=list[p2],list[p1]
    return list
    

list=[10,12,54,60]
print("List before swapping of two elements : ",list)
print("Enter positions where you want to swap the elements : ")
pos1=int(input())
pos2=int(input())
list1=swapping(list,pos1-1,pos2-1)
print("List after swapping of two elements : ",list1)