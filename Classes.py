

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is {self.name}, my color is {self.color} and my weight is {self.weight}")


class Person:
    def __init__(self, name, personality, is_sitting):
        print("base class Person")
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting


    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

"""
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()

r1.introduce_self()
r2.introduce_self()
"""

class Manager(Person):
    def __init__(self):
        print("inherit Person class")
        super().__init__("chief", "white", 100)


#p1 = Person("Alice", "aggressive", False)
h1 = Manager()

