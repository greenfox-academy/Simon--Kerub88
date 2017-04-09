class Garden:
    def __init__(self, water_amount = 4000):
        self.list_flowers = []
        self.list_tree = []
        self.water_amount = water_amount

    def add_tree(self, Tree):
        self.list_tree.append(Tree)

    def add_flower(self, Flower):
        self.list_flowers.append(Flower)

    def watering(self, amount = 40):
        self.amount = amount
        




class Tree(Garden):
    def __init__(self, tree_type, max_water = 20, current_water = 0):
        self.max_water = max_water
        self.current_water = current_water
        self.tree_type = tree_type

class Flower(Garden):
    def __init__(self, flower_type, max_water = 10, current_water = 0):
        self.max_water = max_water
        self.current_water = current_water
        self.flower_type = flower_type


the_garden = Garden()
flower1 = Flower("blue")
the_garden.add_flower(flower1)
print(the_garden.list_flowers[0].current_water)
