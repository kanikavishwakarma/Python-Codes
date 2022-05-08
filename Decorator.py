
# ******************************** DECORATORS ***************************************


def function1():
    print("kanika vishwakarma")
func = function1
func()


def function1():
    print("kanika vishwakarma")
func = function1
del function1
func()


def funcret(num):
    if num == 0:
        return print
    else:
        return int

a=funcret(1)
print(a)

a=funcret(0)
print(a)

def executor(func):
    func("This")

executor(print)    


def dec1(func):
    def nowexec():
        print("Executing now")
        func()
        print("Executed")
    return nowexec    

def kanika():
    print("kanika is a good girl")

dec= dec1(kanika)            
dec()


# USING DECORATORS-----------------------


def dec1(func):
    def nowexec():
        print("Executing now")
        func()
        print("Executed")
    return nowexec    

@dec1
def kanika():
    print("kanika is a good girl")

kanika() 
