
# *********************************** CLASS METHOD AS CONSTRUCTOR ***************************************

class employee:
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

    @classmethod
    def usesplit(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])

karan = employee.usesplit("karan-450-student")
print(karan.salary)        

# OR----------

#     @classmethod
#     def usesplit(cls,string):
#       print(*string.split("-"))
#       return cls(*string.split("-"))
      

# karan = employee.usesplit("karan-450-student")
# print(karan.salary) 
   
