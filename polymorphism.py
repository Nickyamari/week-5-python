class Creature:
    def move(self):
        pass

class Vampire(Creature):
    def move(self):
        print("Flying through the night.")

class Werewolf(Creature):
    def move(self):
        print("Running swiftly across the forest.")

creatures = [Vampire(), Werewolf()]
for creature in creatures:
    creature.move()
