class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Sunflower", 22, 25)
    plant2 = Plant("Rose", 15, 17)
    plant3 = Plant("Magnolia4ever", 25, 34)
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
