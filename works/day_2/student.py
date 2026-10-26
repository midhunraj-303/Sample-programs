# Python program to demonstrate class, objects, constructors and methods
class Student:
    
    def __init__(self, name:str ,age:int, mark:int) -> None:
        """
        Initilize a new student record

        :param name: The name of the student
        :param age: The age of the student
        :param mark: The mark of the student
        """

        self.name = name
        self.age = age
        self.mark = mark

    def display(self):
        """
        Display student details
        """
        print(f"Student name : {self.name}")
        print(f"Student age : {self.age}")
        print(f"Student mark : {self.mark}")
        print("-----------------------\n")

s1 = Student("Manu",22,50)
s2 = Student("Anu",23,45)

s1.display()
s2.display()