class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow_height(self) -> None:
        if self.age in range(0, 30):
            self.height = self.height + 1
        else:
            self.height = self.height + 0.5

    def grow_older(self) -> None:
        self.age = self.age + 1

def ft_plant_factory(plants_data: list) -> None:
    plants = []
    for data in plants_data:
        plant = Plant(data[0], data[1], data[2])
        plants.append(plant)
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    plants_data = [
        ["Rose", 25.0, 30],
        ["Oak", 200.0, 365],
        ["Cactus", 5.0, 90],
        ["Sunflower", 80.0, 45],
        ["Fern", 15.0, 120],
    ]
    print("=== Plant Factory Output ===")
    ft_plant_factory(plants_data)

