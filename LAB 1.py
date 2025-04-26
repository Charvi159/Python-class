Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=5
a+b
15
a-b
5
a*b
50
a/b
2.0
hrs=2
mins=hrs*60
mins
120
mins=180
hrs=mins/60
hrs
3.0
dollar=32
rupees=dollar*48
rupees
1536
rupees=75
dollar=rupees/48
dollar
1.5625
dollars=32
rupees=dollars*48
pounds=rupees/70
pounds
21.942857142857143
grms=500
kgs=grms/1000
kgs
0.5
kgs=2
grms=kgs*1000
grms
2000
byte=2
kbs=byte/1000
mb=byte/1000000

gb=byte/1000000000
kbd
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    kbd
NameError: name 'kbd' is not defined. Did you mean: 'kbs'?
kbs
0.002
mb
2e-06
gb
2e-09
cel=25
f=[(9*cel)/5]+32
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    f=[(9*cel)/5]+32
TypeError: can only concatenate list (not "int") to list
f=((9*cel)/5)+32
f
77.0
f=100
cel=((5/9)*(f-32))
cel
37.77777777777778
p=20000
r=2
n=2
interest=(p*r*n)/100
interest
800.0
len=40
side=40
area=side*side
perimeter=4*side
are
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    are
NameError: name 'are' is not defined. Did you mean: 'area'?
area
1600
perimeter
160

length=20
breadth
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    breadth
NameError: name 'breadth' is not defined
breadth=30
area=length*breadth
peri=2*(length+breadth)
area
600
peri
100
radius=2
area=(22*radius*radius)/7
area
12.571428571428571
h=20
l=10
area=(h*l)/2
area
100.0
gs=50000
al=5000
al=gs*10%
SyntaxError: invalid syntax
al=gs*0.01
ded=gs*0.03
net=gs+al-ded
net
49000.0
al=gs*0.1
ded=gs*0.03
net=gs+al-ded
net
53500.0

gross=5000
>>> dis=gross*0.1
>>> net_sale=gross-dis
>>> net
53500.0
>>> net_sale
4500.0
>>> s1=50
>>> s2=60
>>> s3=55
>>> s1+s2+s3
165
>>> total=s1+s2+s3
>>> avg=total/
SyntaxError: invalid syntax
>>> avg=total/3
>>> total
165
>>> avg
55.0
>>> a=10
>>> b=20
>>> c=a
>>> a=b
>>> b=c
>>> a
20
>>> b
10
