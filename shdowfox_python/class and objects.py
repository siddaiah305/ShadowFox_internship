class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader  

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"

    def check_leader(self):  
        return f"{self.name} is the leader!" if self.leader else f"{self.name} is not the leader."

super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    print(hero.get_info())
    print(hero.check_leader()) 
    print()
