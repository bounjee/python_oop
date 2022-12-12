# Create a Pokemon.
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp


    def __str__(self):
        return f"name: {self.name}, type: {self.primary_type}, hp: {self.hp} / {self.max_hp}"


# Feed them to increase health.

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp}HP.")
        else:
            print(f"{self.name} is full")
# Make them battle and decide for a winner.

    def battle(self, other):
        print("Battle: ", self.name, other.name)
        result =  self.typewheel(self.primary_type, other.primary_type)
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp}HP.")
        print(f"{self.name} fought {other.name} and the result is a {result}")


    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}

        # mapping between types and result conditions
        game_map = {"Water":0, "Fire":1, "Grass":2}
        #implement win-lose
        wl_matrix = [
            [-1, 1, 0],     # water
            [0, -1, 1],     # fire
            [1, 0, -1],     # grass
        ]

        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]



# Take a look at it.
if __name__ == '__main__':
    Bulbasaur = (Pokemon(name="Bulbasaur",primary_type="Grass",max_hp=100))
    Charmender = (Pokemon(name="Charmander",primary_type="Fire",max_hp=150))

    Bulbasaur.battle(Charmender)




