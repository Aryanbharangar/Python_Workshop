class Dog:
    def __init__(self,name):
        self.name=name
dog1=Dog("Buddy")
print(dog1.name)

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
car1=Car("Toyota","Camry")
car2=Car("Honda","Civic")
print(car1.name,car1.model)
print(car2.name,car2.model)



#Encapsulation
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def balance(self):#we can use method only once(__init__) here we have used balce to form a function
        return self.balance# 
account1=BankAccount("12345",1000)
print(account1.account_number)
print(account1.balance())




#Inheritance allowa you  to create new classes that inheritt properties and methods from existing classes.
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(animal):
    def speak(self):
        return "wolf!"
class Cat(animal):
    def speak(self):
        return "Meow!"  
dog=Dog("Buddy")
cat=Cat("Whisker")
print(dog.name,dog.speak())
print(cat.name,cat.speak())
        
    