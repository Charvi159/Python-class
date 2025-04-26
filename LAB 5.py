import random
#1
'''odd_numbers = [random.choice(range(1, 101, 2)) for i in range(5)]
print("List of 5 random odd integers:", odd_numbers)
even_numbers = [random.choice(range(2, 101, 2)) for i in range(4)]
print("List of 4 random even integers:", even_numbers)
odd_numbers[2] = even_numbers
print("Updated list with even integers replacing the third element:", odd_numbers)
flattened_list = [item for sublist in odd_numbers for item in (sublist if isinstance(sublist, list) else [sublist])]
print("Flattened list:", flattened_list)
sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)'''

#2
'''random_integers = [random.randint(1, 100) for i in range(20)]
print("List of 20 random integers:", random_integers)
user_number = int(input("Enter a number to find its positions in the list: "))
positions = [index for index, value in enumerate(random_integers) if value == user_number]
if positions:
    print(f"The number {user_number} is found at positions: {positions}")
else:
    print(f"The number {user_number} is not found in the list.")'''


#3
'''random_integers = [random.randint(1, 30) for i in range(50)]
print("List of 50 random integers:", random_integers)
unique_numbers = list(set(random_integers))
print()
print("List after removing duplicates:", unique_numbers)'''

#4
'''l1=[]
pos=[]
neg=[]
for i in range(20):
    rand_int=random.randint(-10,50)
    l1.append(rand_int)
for i in l1:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print(l1)
print()
print(pos)
print()
print(neg)'''

#5
'''lst=["Eric","Ram","Mohan","Priya","Sita"]
lst_new=[]
for i in lst:
    a=i.upper()
    lst_new.append(a)
print(lst_new)'''

#6
'''lst_f=[32, 50, 77, 104, 212]
lst_c=[]
for i in lst_f:
    c_tmp=(i - 32) * 5/9
    lst_c.append(c_tmp)
print("Fahrenheit:",lst_f)
print("Celsius:",lst_c)'''

#7
'''stack = []
while True:
    print("Stack Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=='1':
        item=input("Enter item to push: ")
        stack.append(item)
        print(item,"pushed into stack.")
    elif choice=='2':
        if stack:
            item=stack.pop()
            print("Popped item: ",item)
        else:
            print("Stack is empty!")
    elif choice=='3':
        if stack:
            print("Stack elements:",stack)
        else:
            print("Stack is empty!")
    elif choice=='4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")'''
#8
'''queue=[]
while True:
    print("Queue Menu:")
    print("1. Enqueue (Add)")
    print("2. Dequeue (Remove)")
    print("3. Display")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=='1':
        item=input("Enter item: ")
        queue.append(item)
        print(item," added to queue.")
    elif choice=='2':
        if queue:
            item=queue.pop(0)
            print("Dequeued item: ",item)
        else:
            print("Queue is empty!")
    elif choice=='3':
        if queue:
            print("Queue elements:", queue)
        else:
            print("Queue is empty!")
    elif choice=='4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")'''

#9
lst1=[1,2,3,4,5,6,7]
lst2=[3,4,7,8,9]
lst3=[]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print("Numbers in list1 but not in list2: ",lst3)


