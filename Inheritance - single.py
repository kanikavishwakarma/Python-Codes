# ************************ SINGLE INHERITANCE *********************************

class employee:
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

        
    def printdetails(self):
        return f"Name is {self.name}.\nSalary is {self.salary}.\nRole is {self.role}"  

class programmer(employee):
    
    def printprog(self):
        return f"Programmer's Name is {self.name}.\nSalary is {self.salary}.\nRole is {self.role}"  


harry = employee("harry",45000,"Instructor")
shubham = programmer("shubham","555","programmer")
print(shubham.printprog())
