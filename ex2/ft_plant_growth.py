class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def grow(self) -> None:
        if self._age in range(0, 30):
            self.height = self.height + 1
        else:
            self.height = self.height + 0.5

    def age(self) -> None:
        self._age = self._age + 1


def ft_plant_growth() -> None:
    plant = Plant("Rose", 20, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    initial_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()
    total_growth = plant.height - initial_height
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
