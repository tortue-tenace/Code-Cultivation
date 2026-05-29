class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow_height(self) -> None:
        if self._age in range(0, 30):
            self._height = self._height + 1
        else:
            self._height = self._height + 0.5

    def grow_older(self) -> None:
        self._age = self._age + 1

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated:  {new_age} days")
        else:
            print(f"{self._name.capitalize()}:  Error, age can't be negative")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated:  {new_height}cm")
        else:
            print(f"{self._name.capitalize()}:  "
                  f"Error, height can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    plant = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:  ", end="")
    plant.show()
    print()
    plant.set_height(25.0)
    plant.set_age(30)
    print()
    plant.set_height(-5.0)
    print("Height update rejected")
    plant.set_age(-10)
    print("Age update rejected")
    print()
    print("Current state:  ", end="")
    plant.show()
