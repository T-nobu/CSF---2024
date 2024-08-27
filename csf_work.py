class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        return f"{self.name} is {self.color} and is {self.age}."
    
dawa = Dog("dawa", "brown", "12")
nima = Dog("nima", "blue", "13")
bruno = Dog("bruno", "white", "14")

print(dawa.bark())
print(nima.bark())
print(bruno.bark())
