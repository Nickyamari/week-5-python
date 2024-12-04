# Parent class: Character (represents a generic character)
class Character:
    def __init__(self, name, age, realm):
        self.name = name
        self.age = age
        self.realm = realm

    def introduce(self):
        return f"I am {self.name}, ruler of the {self.realm}, and I have walked this world for {self.age} years."

    def move(self):
        print(f"{self.name} moves through the realm.")


# Derived class: VampireLord (inherits from Character)
class VampireLord(Character):
    def __init__(self, name, age, realm, power_level):
        super().__init__(name, age, realm)
        self.__power_level = power_level  # Encapsulation: private attribute
        self.is_immortal = True

    def use_magic(self):
        print(f"{self.name} conjures dark magic, striking fear into his enemies!")

    def battle(self):
        self.__power_level -= 10
        print(f"{self.name} fought bravely! His power level is now {self.__power_level}.")

    def replenish_power(self, amount):
        self.__power_level += amount
        print(f"{self.name} has regained strength. His power level is now {self.__power_level}.")

    def turn_human(self):
        self.is_immortal = False
        print(f"{self.name} has turned human and is vulnerable.")

    # Overriding the move() method to demonstrate polymorphism
    def move(self):
        print(f"{self.name} glides silently through the shadows of the night.")


# Another class demonstrating polymorphism: Werewolf
class Werewolf(Character):
    def move(self):
        print(f"{self.name} runs swiftly across the forest, leaving no trace.")


# Example Usage
alexander = VampireLord("Lord Alexander", 500, "Valerian Empire", 100)
werewolf = Werewolf("Fenrir", 300, "Dark Forest")

# Display character introduction and unique behaviors
print(alexander.introduce())
alexander.use_magic()
alexander.battle()
alexander.replenish_power(20)
alexander.move()
alexander.turn_human()

print("\n")

# Demonstrate polymorphism with another creature
werewolf.introduce()
werewolf.move()

