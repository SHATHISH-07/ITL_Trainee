# basic calss implementation
class Student:
    def __init__(self,name, age, native):
        self.name = name
        self.age = age
        self.native = native
        print(f"Student {self.name} as been added to the record")

    def get_student_record(self):
        print(f"{self.name} : {self.age} : {self.native}")

s1 = Student("Sahtish",21,"Salem")
s2 = Student("Kumaran",22,"Chennai")

s1.get_student_record()
s2.get_student_record()

# inheritance
class Animal:
    def speak(self):
        print("Animals makes sound")
    
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
a = Animal()
d.speak()

# encapsulation
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

b = Bank(1000)
print(b.get_balance())