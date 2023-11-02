student={
    "name":"Alice",
    "age":25,
    "Grade":"A"
}
print(student)
print(student.get("name")) # to get value through 
student["city"]="New York"
student["age"]=28
print(student)
for key,value in student.items():
    print(f"{key}:{value}")
for key in student.keys():     # for keys
    print(key)
print(student.values())# output::dict_values(['Alice', 28, 'A', 'New York'])

list=[num**2 for num in range(1,6)]
print(list)

squares={num:num**2 for num in range (1,6)}
print(squares)
