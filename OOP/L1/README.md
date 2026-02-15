# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of organizing software design around real-world objects. Instead of focusing only on functions and logic, OOP models data and behavior together inside structured units called objects. It improves code organization, reusability, scalability, and maintainability.

---

## Concepts of OOP

### 1. Class
A class is a blueprint or template used to create objects. It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

### 2. Object
An object is an instance of a class. It represents a real-world entity and contains both data and behavior defined by its class.

### 3. Attribute (Property)
Attributes are variables defined inside a class that represent the state or characteristics of an object.

### 4. Method
Methods are functions defined inside a class that describe the behaviors or actions an object can perform.

### 5. Constructor
A constructor is a special method that is automatically executed when an object is created. It is commonly used to initialize the object’s attributes.

### 6. Instance vs Class Variables
- Instance variables belong to a specific object.
- Class variables are shared among all instances of the class.

---

## Pillars of OOP

### 1. Encapsulation
Encapsulation is the process of wrapping data and methods together inside a class. It also restricts direct access to some components to protect the integrity of the data.

Purpose:
- Data protection
- Controlled access
- Improved maintainability

### 2. Abstraction
Abstraction hides complex implementation details and shows only the essential features of an object.

Purpose:
- Reduces complexity
- Improves code readability
- Enhances security

### 3. Inheritance
Inheritance allows one class (child/subclass) to acquire the properties and behaviors of another class (parent/superclass).

Purpose:
- Code reusability
- Logical hierarchy
- Reduced redundancy

### 4. Polymorphism
Polymorphism allows objects to take multiple forms. It enables the same method name to behave differently depending on the object.

Types:
- Compile-time Polymorphism (Method Overloading)
- Runtime Polymorphism (Method Overriding)

---

## Class

A class defines a structure for creating objects. It specifies what data the object will hold and what actions it can perform. Classes improve modularity and allow developers to model real-world systems effectively.

Key Characteristics:
- Blueprint for objects
- Contains attributes and methods
- Supports inheritance

---

## Object

An object is a real implementation of a class. When a class is instantiated, an object is created in memory.

Key Characteristics:
- Has state (attributes)
- Has behavior (methods)
- Exists independently in memory

Example Conceptual Model:

Class: Car  
Object: MyCar  

Car defines properties like color and speed.  
MyCar is a specific instance with defined values.

---

## Class Components

A class typically consists of the following components:

1. Attributes  
   Variables that define the object's state.

2. Methods  
   Functions that define behavior.

3. Constructor  
   Initializes object data.

4. Access Modifiers  
   Define visibility and access control (public, private, protected).

5. Static Members  
   Shared across all objects of the class.

---

## Methods

Methods define what an object can do. They operate on the object’s data and may modify or return values.

Types of Methods:
- Instance Methods
- Class Methods
- Static Methods

Method Characteristics:
- Define behavior
- Can take parameters
- Can return values
- Improve modular design

---

## OOP Structure Diagram

```
          +--------------------+
          |        Class       |
          +--------------------+
          | - Attributes       |
          | - Methods          |
          +--------------------+
                   |
                   | creates
                   v
          +--------------------+
          |       Object       |
          +--------------------+
          | State              |
          | Behavior           |
          +--------------------+
```

---

## Advantages of OOP

- Improved code organization
- Better code reusability
- Easier maintenance
- Scalable architecture
- Real-world modeling capability

---

## Conclusion

Object-Oriented Programming provides a structured way to design software by organizing code into reusable and maintainable components. By applying the four pillars—Encapsulation, Abstraction, Inheritance, and Polymorphism—developers can build flexible and scalable systems suitable for real-world applications.
