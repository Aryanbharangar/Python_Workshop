x=15 # here x is global variable 
def add():
    global x  #:it will make the x global 
    global y
    x=10 #x here is an local variable
    y=10
    print(x+y)
print(x+y)
add()
# import random
# m=random.randint(1,100)
# number_tried=0
# while True:
#     n=int(input("Enter a number:"))
#     number_tried+=1
#     if n==m:
#         print("congratulation you gussed the number")
#         break
#     elif n>m:
#         print("Try a smaller number")
#     else:
#         print("Try a larger number")
# print(F"The number of times you attempted:{number_tried}")
