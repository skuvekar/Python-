class Calci: #defining a class called calci

    #defining the init constructor that takes self argument(by default) and the num attribute which is the number entered by the user.
    def __init__(self, num):
        self.num=num

    #defining the square method that returns the result
    def square(self):
        result=pow(self.num,2)
        return result

    #defining the squareroot method that returns the result
    def squareRoot(self):
        result=pow(self.num,(1/2))
        return result
        
    #defining the cube method that returns the result
    def cube(self):
        result=pow(self.num,3)
        return result

#created a list to display it to the user as various options for calci operations
l=['square', 'squareroot', 'cube']

print("The options for calculator are:\n",l)

op=input("\nWhich operations do you want to perform? ")

#will take the input value from the user
x=float(input(f"\nEnter a no.to perform {op}: "))

#object num is created which will pass the input value(collected from user) x as an argument   
num=Calci(x)

#logic to implement the user defined operation
if op=='square':
    r1=num.square()#method square() is called and the result is stored in r1
    print(f"\nThe square of {x} is {r1}")
elif op=='squareroot':
    r2=num.squareRoot()
    print(f"\nThe squareroot of {x} is {r2}")
elif op=='cube':
    r3=num.cube()
    print(f"\nThe cube of {x} is {r3}")
else:
    print("Enter a valid value.")

    






 

