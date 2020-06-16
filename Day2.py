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

