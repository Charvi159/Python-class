#1
'''words=["apple", "banana", "cherry", "date", "elderberry"]
uppercase_words = {word.upper() for word in words}
print("Uppercase Words:", uppercase_words)'''

#2
'''import random
numbers = set(random.randint(15, 45) for i in range(10))
count_less_than_30 = len([num for num in numbers if num < 30])
numbers = {num for num in numbers if num <= 35}
print("Generated Set:", numbers)
print("Count of numbers less than 30:", count_less_than_30)'''

#3
'''names=set()
names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Set after adding names:", names)
names.discard("Charlie")  
names.add("Chris")      
print("Set after modifying a name:", names)
names.discard("Bob")
names.discard("Eve")
print("Set after deleting two names:", names)'''

#4
names={"Alice","Bob","Amanda","Brian","Anna","Blake"}
a_names = {name for name in names if name.startswith("A")}
b_names = {name for name in names if name.startswith("B")}
print("Names starting with 'A':", a_names)
print("Names starting with 'B':", b_names)
