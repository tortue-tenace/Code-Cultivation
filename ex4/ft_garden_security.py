class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self.__age} days old")

    def grow_height(self) -> None:
        if self._age in range(0, 30):
            self._height = self._height + 1
        else:
            self._height = self._height + 0.5

    def grow_older(self) -> None:
        self._age = self._age + 1

    def set_age(self):
        new_age = int(input(f"Enter {self._name.capitalize()} new age: "))
        if new_age >= 0:
            self._age = new_age
            print(f"{self._name.capitalize()} new age updated: {new_age}")
        elif new_age < 0:
            return (print(f"{self._name.capitalize()} age can't be negative"))

    def set_height(self):
        new_height = int(input(f"Enter {self._name.capitalize()}\
         new height: "))
        if new_height >= 0:
            self._height = new_height
            print(f"{self._name.capitalize()}\
             new height updated: {new_height}")
        elif new_height < 0:
            return (print(f"{self._name.capitalize()}\
             height can't be negative"))

    def get_height(self):
        print(self.height)

    def get_age(self):
        print(self.age)


def ft_plant_factory(plants_data: list) -> None:
    plants = []
    for data in plants_data:
        plant = Plant(data[0], data[1], data[2])
        plants.append(plant)
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    plant = Plant("saucisse", 12, 15)
    print(plant._age)
