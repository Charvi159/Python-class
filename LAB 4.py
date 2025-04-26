
#1
'''a='Hello_world'
print(a.upper())
print(a.lower())'''

#2
'''a=int(input("Enter a number:- "))
for i in range(1,11):
    print(a,"x",i,"=",a*i)'''

#3
'''a=input("Enter a string:- ")
count_alpha=0
count_digit=0
for i in a:
    if i.isalpha()==True:
        count_alpha+=1
    elif i.isdigit()==True:
            count_digit+=1
print("Number of alphabets are",count_alpha,"and number of digits are",count_digit)'''

#4
'''num=int(input("Enter a number: "))
# Check for prime
a=num>1
for i in range(2,num):
    if num % i==0:
        a=False
        break
# Check for perfect number
sum_divisors=0
for i in range(1,num):
    if num % i==0:
        sum_divisors+=i
is_perfect=sum_divisors==num
# Check for Armstrong number
sum_armstrong = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** len(str(num))
    temp //= 10
is_armstrong = sum_armstrong == num
# Check for palindrome
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
is_palindrome = reverse == num
# Check for automorphic number
square = num * num
is_automorphic = str(square).endswith(str(num))
print("Prime: ",a)
print("Perfect: ",is_perfect)
print("Armstrong: ",is_armstrong)
print("Palindrome: ",is_palindrome)
print("Automorphic: ",is_automorphic)'''


#5
'''for a in range(1,31):
    for b in range(a,31):  
        c=(a**2+b**2)**0.5
        if c.is_integer()and c<=30: 
            print(a,b,int(c))'''
#6
'''for hour in range(24):
    if hour==0:
        suffix="Midnight"
    elif hour==12:
        suffix="Noon"
    elif hour<12:
        suffix="AM"
    else:
        suffix="PM"

    print(hour,':00',suffix)'''

#7
'''import math
n=int(input("Enter n: "))
r=int(input("Enter r: "))
nCr=math.factorial(n)//(math.factorial(r)*math.factorial(n - r))
nPr=math.factorial(n)//math.factorial(n - r)
print("nCr (Combination): ",nCr)
print("nPr (Permutation): ",nPr)'''

#8
'''a=int(input("Enter number:- "))
fac=0
for i in range(1,a):
    fac=a*i
print("Factorial is ",fac)'''

#9
'''a=int(input("Enter a number: "))
for i in range(a,0,-1):
    print(i)'''

#10
'''no=int(input("Enter the number of terms: "))
a,b=0,1
print("Fibonacci Series:")
for i in range(no):
    print(a)
    a,b=b,a+b'''

#11
import math
x = float(input("Enter the radian value: "))
term=x
sin_x =x
n=1
sign=-1
while abs(term)>1e-10:
    term=(x**(2*n + 1)) / math.factorial(2*n + 1)
    sin_x+=sign*term
    sign*=-1
    n+=1
    
# Print the approximated sin(x)
print("sin(",x,")=",sin_x)
