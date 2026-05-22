class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__age = age
        self.__height = height

    def show(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def grow_height(self) -> None:
        if self.__age in range(0, 30):
            self.__height = self.__height + 1
        else:
            self.__height = self.__height + 0.5

    def grow_older(self) -> None:
        self.__age = self.__age + 1
    
    def set_age(self):
        new_age = int(input(f"Enter {self.__name.capitalize()} new age: "))
        if new_age >= 0:
            self.__age = new_age
            print(f"{self.__name.capitalize()} new age updated: {new_age}")
        elif new_age < 0:
            return(print(f"{self.__name.capitalize()} age can't be negative"))

    def set_height(self):
        new_height = int(input(f"Enter {self.__name.capitalize()} new height: "))
        if new_height >= 0:
            self.__height = new_height
            print(f"{self.__name.capitalize()} new height updated: {new_height}")
        elif new_height < 0:
            return (print(f"{self.__name.capitalize()} height can't be negative"))

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
    plant.set_age()
    plant.set_height()