# ------------------------------
# Assignment 1: Design Your Own Class! 🏗️
# ------------------------------

# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # encapsulated (private attribute)

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_storage(self):
        return self.__storage

    def add_storage(self, amount):
        self.__storage += amount
        print(f"Storage upgraded! Total storage: {self.__storage}GB")


# Child Class (Inheritance + Polymorphism Example)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)
        self.gpu_power = gpu_power

    # Polymorphism: Overriding method
    def call(self, number):
        print(f"{self.brand} {self.model} starts a video call with {number} 🎮")


# ------------------------------
# Activity 2: Polymorphism Challenge! 🎭
# ------------------------------

class Animal:
    def move(self):
        print("The animal moves...")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies 🕊️")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")


if __name__ == "__main__":
    # Assignment 1 Demo
    phone1 = Smartphone("Samsung", "S22", 128)
    phone1.call("123-456-789")
    phone1.add_storage(64)

    gphone = GamingPhone("Asus", "ROG Phone 6", 256, "Ultra GPU")
    gphone.call("987-654-321")
    print("Storage (encapsulated):", gphone.get_storage())

    print("\n--- Polymorphism Challenge 🎭 ---")
    animals = [Dog(), Bird(), Fish()]

    for animal in animals:
        animal.move()
