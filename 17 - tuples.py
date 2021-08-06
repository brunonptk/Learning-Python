# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bruno",23,"male")

print(student.count("Bruno"))
print(student.index("male"))

for x in student:
    print(x)

if "Bruno" in student:
    print("Bruno is here!")