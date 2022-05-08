class employee:
    var = 10
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

        
    def printdetails(self):
        return f"Name is {self.name}.\nSalary is {self.salary}.\nRole is {self.role}"

class player:
    var = 9
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name} and game is {self.game}" 

class coolprogrammer(player,employee):

    language = "c++"
    def printlanguage(self):
        print(self.language)

harry = employee("harry",45000,"Instructor")
shubham = employee("shubham","555","student")        

rohan = player("rohan",["cricket"])
karan = coolprogrammer("karan",["soccer"])

print(karan.var)
