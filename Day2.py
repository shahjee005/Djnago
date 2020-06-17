#Control Flow 
#Conpareson Operators 

#Greater than 
1>2


#Less than 
1<2
1>=1
1>=4
#equality 

1==1
1=='1' 
'hi'== 'bye'
#inequality 
1!=2
if 1<2:
    print('yes!')

if 1 >2:
    print ("true!")
else: 
    print ('!True')

if 1==1:
    if 1>2:
        print ("hello")
    elif 3==3:
        print ('elif ran')
    else:
        print ('last')

#Loops
#for loop
#Pairs 
# While loops 
i=1 
while i<5:
    print ("1 is :{}".format(i))
    i=i+1
#Range function 
for item in range( 8):
    print (item)


#List comprehension
x= [1,2,3,4]
out =[]

for num in x :
    out.append(num**2)
print (out)

#abother methord
out =[num**2 for num in x]
print (out)


print(2+2)

#OOP (Object oriented programming)
mylist =[1,2,3]
mylist.append(4)
print(mylist)

print (type([1,2,3])) # list  
print (type(()))  # tuple 

####ClASS
class Sample ():     # (class names are always starts with capital letter)
    pass
x = Sample ()
print(type(x))
# Lets define another class



###Attributes 

class Dog():

#Class object attribute 
    Species = "mamal"
    def __init__(self,breed, name):
        self.breed= breed
        self.name = name 
mydog = Dog(breed = 'Lab', name = "Sammy") #OR 
mydog = Dog('Lab',"Sammy") # Most likely used 
#otherdog = Dog(breed= "Huskie")
print(mydog.breed)
print(mydog.name)
print(mydog.Species)
#print(otherdog.breed)


### Another example of Class####
class Circle ():
    pi =3.14
    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius= 1):
        self.radius = radius
    # Method for resetting Radius
    def area(self):
        return self.redius* self.radius * Circle.pi 
    # Method for resetting Radius
    def setRadius(self,radius):
        self.radius =radius
    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius

c = Circle()

c.setRadius(2)
print ('Radius is: ',c.getRadius())
print ('Area is: ',c.area())