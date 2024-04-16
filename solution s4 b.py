# A Python program to demonstrate inheritance Inherit a TV class add additional properties like screen thickness,
#energy usage , Lifespan , Refresh rate , functionalities like viewingAngle ,
#Backlight, DisplayDetails , which displays the detailed features of the TV
class TV (object):
# Constructor
    def __init__(self, properties):
	    self.properties = properties

# To check if this person is an employee
def Display(self):
	print(self.properties)


# Driver code
emp = Tv ("Satyam", 102) # type: ignore # An Object of Person
emp.Display()

class LED(TV ):

    def Print(self):
	    print("screen thickness")
	
LED_details = LED("Mayank", 103)

# calling parent class function
LED_details.Display()

# Calling child class function
LED_details.Print()
