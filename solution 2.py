#2 Create proper member variables inside the task if required and use them when necessary.For example for this task
# create a class private variable named pi=3.141
class mclass:  
    __privateVariable1 = 2018;  
    def __privateMethod1(self):  
        print("I'm inside the class mainclass which this is private method")  
    def iclass(self):  
        print("Private Variable: ",mclass.__privateVariable1)  
        self.__privateMethod1()  
foo = mclass()  
print("private variable value pi=3.141")