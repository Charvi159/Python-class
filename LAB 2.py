#1
'''a=int(input('Enter first number:-'))
b=int(input('Enter second number:-'))
if a>b:
    print(a,'is the largest number')
else:
    print(b,'is the largest number')
if a<b:
    print(a,'is the smallest number')
else:
    print(b,'is the smallest number')'''


#2
'''a=int(input('Enter first number:-'))
b=int(input('Enter second number:-'))
c=int(input('Enter third number:-'))
#largest
if (a>b and a>c):
    print(a,'is the largest number')
elif (b>a and b>c):
    print(b,'is the largest number')
else:
    print(c,'is the largest number')
#smallest
if (a<b and a<c):
    print(a,'is the smallest number')
elif (b<a and b<c):
    print(b,'is the smallest number')
else:
    print(c,'is the smallest number')'''


#3
'''a=int(input('Enter a number:-'))
if (a%2==0):
    print(a,'is an even number')
else:
    print(a,'is an odd number')'''


#4
'''a=int(input('Enter a number:-'))
if (a%10==0):
    print(a,'is divisible by 10')
else:
    print(a,'is not divisible by 10')'''


#5
'''a=int(input('Enter age:-'))
if (a>=18):
    print('Major')
else:
    print('Minor')'''


#6
'''a=input('Enter a number:-')
if (a != '\0'):
    print(a)'''
    
#7
'''a=int(input('Enter year:-'))
if (a%4==0):
    print('The year is a leap year')
else:
    print('The year is not a leap year')'''


#8
'''a=int(input('Enter the first angle:-'))
b=int(input('Enter the second angle:-'))
c=int(input('Enter the third angle:-'))
if (a+b+c==180):
    print('The triangle is valid')
else:
    print('The triangle is invalid')'''

#9
'''number=float(input("Enter a number: "))
print("The absolute value is:", abs(number))'''

#10
'''l=int(input('Enter the length of the rectangle:-'))
b=int(input('Enter the breadth of the rectangle:-'))
area=l*b
peri=2*(l+b)
if (area>peri):
    print('Area is greater than the perimeter')
else:
    print('Perimeter is greater than the area')'''

#11
'''x1=float(input('Enter the first coordinate x1:- '))
y1=float(input('Enter the first coordinate y1:- '))
x2=float(input('Enter the second coordinate x2:- '))
y2=float(input('Enter the second coordinate y2:- '))
x3=float(input('Enter the third coordinate x3:- '))
y3=float(input('Enter the third coordinate y3:- '))
slope1=(y2-y1)/(x2-x1)
slope2=(y3-y2)/(x3-x2)
if(slope1==slope2):
    print('The points lie in a straight line')
else:
    print('The points do not lie in a straight line')'''

#12
'''import math
x_center=float(input("Enter the x-coordinate of the circle's center: "))
y_center=float(input("Enter the y-coordinate of the circle's center: "))
radius=float(input("Enter the radius of the circle: "))
x_point=float(input("Enter the x-coordinate of the point: "))
y_point=float(input("Enter the y-coordinate of the point: "))
dist=math.sqrt(pow((x_point-x_center),2)+pow((y_point-y_center),2))
if dist<radius:
    print("The point lies inside the circle.")
elif dist==radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")'''

#13
'''d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
a=int(input("Enter a number between 0 and 19:"))
if 0<=a<=19:
    print("The equivalent word is:",d[a])
else:
    print("Please enter a valid number between 0 and 19.")'''

#14
a=int(input("Enter the marks of subject 1:- "))
b=int(input("Enter the marks of subject 2:- "))
c=int(input("Enter the marks of subject 3:- "))
total=a+b+c
avg=total/3
print('Total marks:- ',total)
print('Average marks:- ',avg)
for i in range(3):
    if (a or b or c)<= 39:
        print("grades='F'")
    elif (a or b or c) <= 44:
        print("grades='P'")
    elif (a or b or c) <= 49:
        print("grades='C'")
    elif (a or b or c) <= 54:
        print("grades='B+'")
    elif (a or b or c) <= 59:
        print("grades='B'")
    elif (a or b or c) <= 69:
        print("grades='A'")
    elif (a or b or c) <= 79:
        print("grades='A+'")
    else:
        print("grades='O'")


    
    
