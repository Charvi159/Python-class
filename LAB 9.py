#9:- a
#1
'''def count_lower_upper(s):
    lower=0
    upper=0
    for i in s:
        if i.islower():
            lower+=1
        else:
            upper+=1
    print({'upper case count':upper,'lower case count':lower})

count_lower_upper("PyTHon")'''


#2
'''def compute(a):
    add=0
    for i in range(1,a+1):
        cond=a**i
        add+=cond
    print('sum=',add)

user=int(input("Enter the number:- "))
compute(user)'''

#3
'''def create_array(x,y,z,value):
    return [[[value] * z for _ in range(y)] for _ in range(x)]
array=create_array(2,3,4,5)
print(array)'''

#4
'''def sum_avg(lst):
    tot=0
    for i in lst:
        tot+=i
    avg=tot/5
    print( tot)
    print( avg)
sum_avg([20,30,40,50,10])'''

#5
'''def ispanagram(a):
    a_set=set(a)
    count=0
    for i in a_set:
        if i.isalpha():
            if count==0:
                count+=1
    print(count)
ispanagram('Crazy Fredrick bought many very exquisite opal jewels')'''

#6
'''def tuples(n):
    for x in range(1,n+1):
        lst=[]
        a=(x,x**2,x**3)
        tup=tuple(a)
        lst.append(tup)
        print(lst)
end_value=int(input("Enter end value:- "))
tuples(end_value)'''

#7
'''def ispalindrome(s):
    new_s= s.replace(" ","").lower()
    if (new_s==new_s[::-1]):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')
        
a=input("Enter a string:- ")
ispalindrome(a)'''

#8
'''def convert(s):
    words=s.split()
    unique_words=list(set(words))
    sorted_words=sorted(unique_words)
    return " ".join(sorted_words)
input_string ="banana apple banana orange apple"
result=convert(input_string)
print(result)'''

#9
'''def count_alpha_digits(d_a):
    count_alpha=0
    count_digit=0
    for i in d_a:
        if i.isalpha()==True:
            count_alpha+=1
        elif i.isdigit()==True:
            count_digit+=1
    print({'Number of alphabets':count_alpha,'Number of digits':count_digit})
a=input("Enter a string:- ")
count_alpha_digits(a)'''
    
#10
'''def frequency(a):
    freq_wrds=0
    for i in a:
        if i.isalpha():
            freq_wrds+=1
    print(freq_wrds)
frequency("Python is a programming language")'''

#11
'''def create_list(a,b):
    lst=[]
    for i in a:
        for j in b:
            if i==j:
                lst.append(i)
    print(lst)
create_list([1,2,3,4],[2,3,5,1])'''


#RECURSIVE FUNCTIONS
#1
'''def prime_factors(n, divisor=2):
    if n < 2:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    return prime_factors(n, divisor + 1)
num = 56
result = prime_factors(num)
print("Prime Factors:", result)'''

#2
'''def to_binary(n):
    return bin(n)[2:] 
num = 25
print("Binary Equivalent:", to_binary(num))'''

#3
'''def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in "aeiou") + count_vowels(s[1:])
input_string = "Hello World"
print("Vowel Count:", count_vowels(input_string))'''

#4
'''def reverse_list(lst):
    if not lst:  
        return []
    return [lst[-1]] + reverse_list(lst[:-1])
numbers = [1, 2, 3, 4, 5]
print("Reversed List:", reverse_list(numbers))'''

#5
'''def power(a, b):
    if b==0:
        return 1  
    return a*power(a,b-1)
a = 2
b = 3
print("{a}^{b} =", power(a, b))'''

#6
'''def sanitize_list(lst):
    if not lst:
        return []  
    return [max(0, lst[0])] + sanitize_list(lst[1:])  

numbers = [-3, 5, -1, 0, 8, -6]
print("Sanitized List:", sanitize_list(numbers))'''

#7
'''def average(lst, count=0, total=0):
    if not lst:
        return total / count if count > 0 else 0 
    return average(lst[1:], count + 1, total + lst[0]) 
numbers = [5, 10, 15, 20]
print("Average:", average(numbers))'''

#8
'''def string_length(s):
    if not s:
        return 0  
    return 1 + string_length(s[1:])  
input_string = "Hello"
print("Length of string:", string_length(input_string))'''

#9:- b
#1
'''def fun():
    return 'HI'
def disp():
    return 'HELLO'
def msg():
    return 'NAMASTE'
lst=[fun,disp,msg]
a=list(map(lambda x:x(),lst))
print(a)'''

#2
'''l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]
a=list(map(lambda x,y:x+y,l1,l2))
print(a)'''

#3
'''import random
lst=list(random.randint(-15,15) for i in range(10))
print(lst)
a=list(map(lambda x:x**2,lst))
print(a)'''

#4
'''lst=['madam','filter','malayalam',12321]
a=list(filter(lambda x:str(x)==str(x) [::-1],lst))
print(a)'''

#5
lst=['shivanshi','priyansh','reyansh']
a=list(filter(lambda x:len(x)>=8,lst))
print(a)

