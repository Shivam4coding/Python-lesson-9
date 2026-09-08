#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them

class student:
    grade=9
    name="Shivam"

    def introduction(self):
        print("I am a student")
    def details(self):
        print("My name is", self.name)
        print("My grade is", self.grade)

ob=student()
ob.introduction()
ob.details()
