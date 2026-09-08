class Robot:
    species = "robot"

    def __init__(self, name, age):
        self.name = name
        self.age = age


r1 = Robot("Robo", 2)
r2 = Robot("Nova", 5)

print("Hello! My name is {}.".format(r1.name))
print("I am a {}.".format(r1.species))
print("I am {} years old.".format(r1.age))

print()

print("Hello! My name is {}.".format(r2.name))
print("I am also a {}.".format(r2.species))
print("I am {} years old.".format(r2.age))