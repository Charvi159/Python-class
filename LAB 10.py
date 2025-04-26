#1
'''import csv as c
f=open("a.csv","w")
r=c.reader(f)
w=c.writer(f)
w.writerow([1,2,3])
f.close()'''

#2
'''import csv
students_dict = {}
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        rollno, name, subject1, subject2, subject3 = map(str, row)
        total = int(subject1) + int(subject2) + int(subject3)
        students_dict[rollno] = {"Name": name, "Marks": [int(subject1), int(subject2), int(subject3)], "Total": total}
print(students_dict)'''

#3
'''def create_vcard(name, phone, email, filename="contact.vcf"):
    vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    with open(filename, "w") as file:
        file.write(vcard_data)
    print(f"vCard saved as {filename}")
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
create_vcard(name, phone, email)'''

#4
'''source_subdir = "source_folder"
new_subdir = "destination_folder"
file_to_copy = "example.txt"
try:
    with open(f"{source_subdir}/{file_to_copy}", "r") as source_file:
        content = source_file.read()      
    with open(f"{new_subdir}/{file_to_copy}", "w") as dest_file:
        dest_file.write(content)
        print(f"File '{file_to_copy}' copied to '{new_subdir}' successfully!")
except FileNotFoundError:
    print("Error: Source file not found!")'''

#5
'''f1=open("input1.txt",mode='r')
f=open("input.txt",mode='w')
ch=f1.read()
for i in ch:
    a=ch.upper()
f.write(a)
f.close()
f1.close()'''

#6
'''def merge_files(file1, file2, output_file):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
        for line1, line2 in zip(lines1, lines2):
            out.write(line1)
            out.write(line2)

        remaining_lines = lines1[len(lines2):] + lines2[len(lines1):]
        out.writelines(remaining_lines)

    print(f"Merged file saved as '{output_file}'")
merge_files("file1.txt", "file2.txt", "merged_output.txt")'''

#7
'''def serialize_employee(empcode, empname, joining_date, salary, filename="employee_data.txt"):
    with open(filename, "w") as file:
        file.write(f"{empcode},{empname},{joining_date},{salary}")
    print("Employee data serialized successfully!")
def deserialize_employee(filename="employee_data.txt"):
    with open(filename, "r") as file:
        data = file.read().split(",") 
        return data  
empcode = "E101"
empname = "Alice"
joining_date = "2022-05-15"
salary = "50000"
serialize_employee(empcode, empname, joining_date, salary)
employee_data = deserialize_employee()
print("Deserialized Employee Data:", employee_data)'''

#8
'''f=open("original.txt",mode='r')
f1=open("new.txt",mode='w')
a=f.read()
l=list(a.split())
t=[]
for i in l:
    if i=='a' or i=='an' or i=='the':
        t.append(" ")
    else:
        t.append(i)
for i in t:
    f1.write(i)
    f1.write(' ')
f.close()
f1.close()'''



