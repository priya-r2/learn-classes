# OOP
# DRY
# encapsulation
# abstraction
# inheritence
# polymorphism

class game_character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run_game(self):
        print(f"{self.name} is running game in level1")

class wizard(game_character):
    def __int__(self, name, age):
        super.__init__(name, age)
    def attack(self):
        print("attacking with wand")

class archer(game_character):
    def __int__(self, name, age):
        super.__init__(name, age)
    def attack(self):
        print("attacking with arrows")


char1 = game_character("player1", 25)
char2 = wizard("player2", 35)
char3 = archer("player3", 10)
char1.run_game()
char2.attack()
char2.run_game()
char3.attack()
char3.run_game()