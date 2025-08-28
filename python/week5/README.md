
# Python OOP Assignments 🐍

This project demonstrates key **Object-Oriented Programming (OOP)** concepts in Python:  
- Classes & Objects 🏗️  
- Constructors (`__init__`)  
- Encapsulation 🔒  
- Inheritance 👑  
- Polymorphism 🎭  

---

## Assignment 1: Design Your Own Class 🏗️
We built a `Smartphone` class with:
- Attributes: `brand`, `model`, `storage` (encapsulated as `__storage`).  
- Methods: `call()`, `get_storage()`, `add_storage()`.  
- A subclass `GamingPhone` that **inherits** from `Smartphone` and overrides the `call()` method (demonstrating **polymorphism**).  

### Example
```python
phone1 = Smartphone("Samsung", "S22", 128)
phone1.call("123-456-789")
phone1.add_storage(64)

gphone = GamingPhone("Asus", "ROG Phone 6", 256, "Ultra GPU")
gphone.call("987-654-321")   # Overridden call method
print("Storage:", gphone.get_storage())
````

---

## Activity 2: Polymorphism Challenge 🎭

Created multiple `Animal` classes, each with its own version of the `move()` method:

* `Dog.move()` → 🐕 "The dog runs"
* `Bird.move()` → 🕊️ "The bird flies"
* `Fish.move()` → 🐟 "The fish swims"

### Example

```python
animals = [Dog(), Bird(), Fish()]
for a in animals:
    a.move()
```

Output:

```
The dog runs 🐕
The bird flies 🕊️
The fish swims 🐟
```

---

