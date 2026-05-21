class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        if self.age in range(0, 30):
            self.height = self.height + 1
        else:
            self.height = self.height + 0.5

    def grow_older(self):
        self.age = self.age + 1


def ft_plant_growth():
    plant = Plant("Rose", 20, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    initial_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.grow_older()
        plant.show()
    total_growth = plant.height - initial_height
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
