#1 Create a program class called circle with constructor which will take a list as an argument for the task.
#The List is[10,501,22,37,100,999,87,351]
class Circle:
# constructor
    def __init__(self):
# initializing instance variable
        self.num=[10,501,22,37,100,999,87,351]

# a method
def read_number(self):
    print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj

try:
    print([10,501,22,37,100,999,87,351])
 
    # AttributeError while accessing
    # in the existing method
    print(obj.second)
except:
    print("No such Attribute")