#1
'''lst=[("Eric",),("Ram",),("Mohan",),"Priya","Sita"]
b_count=0
g_count=0
for j in lst:
    if isinstance(j, tuple):
        b_count+=1
    else:
        g_count+=1
print(b_count)
print(g_count)

#2
lst=[(1,'Eric',12),(2,'Shyam',13),(3,'Priya',18)]
rno=[]
nme=[]
age=[]
for i in lst:
    rno.append(i[0])
    nme.append(i[1])
    age.append(i[2])
print(rno)'''

#3
'''from datetime import date
date1 = (12, 2, 2025)
date2 = (25, 3, 2025)
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])
delta = abs((d2 - d1).days)
print("THE NUMBER OF DAYS ARE:- ",delta)'''

#4
lst=[('Pizza',80),('Apple',20),('Banana',30)]
for i in lst:
    for j in (lst-1):
        sort(lst,ascending=False)

#5
'''lst=[(),(1,2),(3,4,5),()]
for i in lst:
    if len(i)==0:
        lst.remove(i)
print(lst)'''

#6
'''tup=("Eric","Ram","Mohan","Priya","Sita")
print("Original tuple:- ",tup)
lst=list(tup)
mod=input("Enter the name to be modified:- ")
for i in range(len(lst)):
    if lst[i]==mod:
        a=input("Enter the new element:- ")
        lst.pop(i)
        lst.insert(i,a)
new_tup=tuple(lst)
print("Modified tuple:- ",new_tup)'''

#7
tup=("Eric","Ram","Mohan","Priya","Sita")
print("Original tuple:- ",tup)
lst=list(tup)
a=int(input("Enter the index to be removed:- "))
for i in range(len(lst)):
    if i==a:
        lst.pop(i)
mod=tuple(lst)
print("Modified tuple:- ",mod)
