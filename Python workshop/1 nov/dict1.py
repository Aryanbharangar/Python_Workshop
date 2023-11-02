# student={
#     "name":"Alice",
#     "age":25,
#     "Grade":"A"
# }

# del student["age"]
# print(student)
# print(student.get("village","N/A"))
# print(student.update({"village":"NG"}))
# print(student)
# dic1={1:10}
# dic2={2:10}
# dic1.update(dic2) #to add the two or more dictonary...
# print(dic1)

dict={1:2,3:6,6:5,5:5}
inp=eval(input("enter key name:"))
if inp in dict.keys():
    print("The key is present in dictonary")
else:
    print("Key is not present")
