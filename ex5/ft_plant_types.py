class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def growheight(self) -> None:
        if self.age in range(0, 30):
            self.height = self.height + 1
        else:
            self.height = self.height + 0.5

    def grow_older(self) -> None:
        self.age = self.age + 1

    def setage(self) -> None:
        newage = int(input(f"Enter {self.name.capitalize()} new age: "))
        if newage >= 0:
            self.age = newage
            print(f"{self.name.capitalize()} new age updated: {newage}")
        elif newage < 0:
            return (print(f"{self.name.capitalize()} age can't be negative"))

    def setheight(self) -> None:
        newheight = int(input(f"Enter {self.name.capitalize()}\
         new height: "))
        if newheight >= 0:
            self.height = newheight
            print(f"{self.name.capitalize()}\
             new height updated: {newheight}")
        elif newheight < 0:
            return (print(f"{self.name.capitalize()}\
             height can't be negative"))

    def getheight(self) -> None:
        print(self.height)

    def getage(self) -> None:
        print(self.age)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom:
            print(f"{self.name.capitalize()} has bloomed")
        else:
            print(f"{self.name. capitalize()} has not bloomed yet")

    def bloomed(self) -> None:
        if not self.bloom:
            self.bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        if self.height == 0 or self.trunk_diameter == 0:
            print(f"{self.name.capitalize()} produces no shade.")
        else:
            print(f"Tree {self.name.capitalize()} now produces a shade of "
                  f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloomed()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 15)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.growheight()
        tomato.grow_older()
    tomato.show()
