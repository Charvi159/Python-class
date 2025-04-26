#1
'''animals={'Tiger':141,'Lion':663,'leopard':110}
birds={'Eagle':38,'Sparrow':450,'Parrot':200}
pets={'Dog':50,'Cat':32,'Birds':20,'Fish':10}
combined={**animals,**birds,**pets}
print(combined)'''

#2
'''d ={ }
if d==dict():
    print('Empty Dictionary.')
else:
    print('Not Empty')'''

#3
employees = [{"dept_no": 101, "roll_no": 1, "salary": 5000},{"dept_no": 102, "roll_no": 2, "salary": 6000},{"dept_no": 101, "roll_no": 3, "salary": 5500},{"dept_no": 102, "roll_no": 4, "salary": 7000},{"dept_no": 103, "roll_no": 5, "salary": 8000}]
dept_salaries = {}
for i in employees:
    dept_no = i["dept_no"]
    salary = i["salary"]
    if dept_no not in dept_salaries:
        dept_salaries[dept_no]=[]
    dept_salaries[dept_no].append(salary)
    
for dept_no, salaries in dept_salaries.items():
    min_salary=min(salaries)
    max_salary=max(salaries)
    print("Department=",{dept_no},"Min Salary=",{min_salary},"Max Salary=",{max_salary})

#4
'''a=input('Enter a string:-')
list(a)
length=len(a)
d={}
freq=0
for i in a:
    if i not in d:
        d[i]=freq
    freq=freq+1
print(d)'''
 
#5
'''d1={'soap':70,'shampoo':150,'napkin':50,'tub':70}
d2={'soap':2,'shampoo':2,'napkin':3,'tub':1}
price=0
for i in d1:
    if i in d2:
        price=(d1[i]*d2[i])+price
print(price)'''
