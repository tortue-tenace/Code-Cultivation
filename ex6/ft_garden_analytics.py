class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f"Stats:  {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{self._height}cm, {self._age} days old")
        self._stats._show_calls += 1

    def grow(self) -> None:
        if self._age in range(0, 30):
            self._height = round(self._height + 1, 1)
        else:
            self._height = round(self._height + 0.5, 1)
        self._stats._grow_calls += 1

    def age(self) -> None:
        self._age = self._age + 1
        self._stats._age_calls += 1

    def set_age(self, newage: int) -> None:
        if newage >= 0:
            self._age = newage
            print(f"{self._name.capitalize()} age updated: {newage}")
        else:
            print(f"{self._name.capitalize()}: Error, age can't be negative")

    def set_height(self, newheight: float) -> None:
        if newheight >= 0:
            self._height = newheight
            print(f"{self._name.capitalize()} height updated: {newheight}")
        else:
            print(f"{self._name.capitalize()}: "
                  f"Error, height can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color:  {self._color}")
        if self._bloomed:
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            print(f"Stats:  {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats: "Tree.Stats" = Tree.Stats()

    def produce_shade(self) -> None:
        if self._height == 0 or self._trunk_diameter == 0:
            print(f"{self._name.capitalize()} produces no shade.")
        else:
            print(f"Tree {self._name.capitalize()} now produces a shade of "
                  f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._stats._shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter:  {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season:  {self._harvest_season.capitalize()}")
        print(f"Nutritional value:  {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self) -> None:
        super().bloom()

    def show(self) -> None:
        super().show()
        print(f"Seeds:  {self._seeds}")


def display_stats(plant: Plant) -> None:
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year?  -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year?  "
          f"-> {Plant.is_older_than_a_year(400)}")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower._seeds = 42
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)
