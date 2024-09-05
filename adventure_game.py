class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def describe(self):
        print(f"{self.name} has {self.health} health and the following items: {self.inventory}")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def pick_item(self, item):
        self.inventory.append(item)

class Hero(Character):
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100  

class Villain(Character):
    def describe(self):
        print(f"{self.name} is a fearsome villain with {self.health} health and the following items: {self.inventory}")

class Adventure:
    def __init__(self):
        self.characters = []
        self.scenes = {}

    def add_scene(self, name, description):
        self.scenes[name] = description

    def play_scene(self, name):
        if name in self.scenes:
            print(f"Scene: {name}")
            print(self.scenes[name])
        else:
            print(f"The scene {name} does not exist.")

archer = Hero("Archer")
goblin = Villain("Goblin")

adventure = Adventure()
adventure.add_scene("Forest", "You are in a dark forest. There's a shiny object on the ground.")
adventure.add_scene("Cave", "The cave is dark and you can hear growling.")

adventure.play_scene("Forest")

archer.pick_item("Shiny Sword")

archer.describe()

adventure.play_scene("Cave")

archer.take_damage(20)

archer.describe()