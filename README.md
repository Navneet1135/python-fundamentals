# 🐍 Python Fundamentals Practice

This repository contains beginner-level Python programs with **definitions and solved examples** for each topic and subtopic.

---

## 📚 Topics Covered

---

## 🔹 1. Type Conversion

**Definition:**  
Type conversion means converting one data type into another.

### Subtopics:

- **Boolean to String**
  - Definition: Converts boolean value into string  
  - Example:
    result = str(True)   # "True"

- **String to Integer**
  - Definition: Converts string number into integer  
  - Example:
    result = int("10")   # 10

- **Integer to Float**
  - Definition: Converts integer into decimal number  
  - Example:
    result = float(5)    # 5.0

---

## 🔹 2. String Operations

**Definition:**  
String operations are used to manipulate text data.

### Subtopics:

- **Indexing**
  - Definition: Access characters using position  
  - Example:
    text = "Python"
    print(text[0])   # P

- **Negative Indexing**
  - Definition: Access characters from end  
  - Example:
    print(text[-1])  # n

- **Slicing**
  - Definition: Extract part of string  
  - Example:
    print(text[0:3])  # Pyt

- **Length**
  - Definition: Count total characters  
  - Example:
    print(len(text))  # 6

- **Concatenation**
  - Definition: Join two strings  
  - Example:
    print("Hello " + "World")  # Hello World

- **Escape Sequences**
  - Definition: Special characters like new line or tab  
  - Example:
    print("Hello\nWorld")

- **Case Conversion**
  - Definition: Change text case  
  - Example:
    print(text.upper())  # PYTHON

- **Replace**
  - Definition: Replace characters in string  
  - Example:
    print(text.replace("P", "J"))  # Jython

---

## 🔹 3. List in Python

**Definition:**  
A list is a collection of items that is **ordered and mutable**.

### Subtopics:

- **Creating List**
  - Example:
    numbers = [10, 20, 30]

- **Adding Elements**
  - Definition: Add new item using `append()`  
  - Example:
    numbers.append(40)

- **Removing Elements**
  - Definition: Remove item using `remove()`  
  - Example:
    numbers.remove(20)

---

## 🔹 4. Tuple in Python

**Definition:**  
A tuple is a collection of items that is **ordered but immutable**.

### Subtopics:

- **Creating Tuple**
  - Example:
    numbers = (10, 20, 30)

- **Accessing Elements**
  - Example:
    print(numbers[0])  # 10

---

## 🔹 5. List & Tuple Concepts

**Definition:**  
Used to access and manipulate structured data.

### Subtopics:

- **Nested List**
  - Definition: List inside list  
  - Example:
    nested = [[1, 2], [3, 4]]
    print(nested[1][1])  # 4

- **Nested Tuple**
  - Example:
    nested = ((1, 2), (3, 4))
    print(nested[1][1])  # 4

- **Negative Indexing**
  - Example:
    nums = [10, 20, 30]
    print(nums[-1])  # 30

- **Slicing**
  - Example:
    print(nums[0:2])  # [10, 20]

---

## 🔹 6. Set in Python

**Definition:**  
A set is a collection of **unique and unordered elements**.

### Subtopics:

- **Creating Set**
  - Example:
    my_set = {1, 2, 2, 3}
    print(my_set)  # {1, 2, 3}

- **Adding Elements**
  - Example:
    my_set.add(4)

- **Removing Elements**
  - Example:
    my_set.remove(2)

---

## 🔹 7. Set Operations

**Definition:**  
Used to perform mathematical operations on sets.

### Subtopics:

- **Union**
  - Definition: Combine both sets  
  - Example:
    print(A | B)

- **Intersection**
  - Definition: Common elements  
  - Example:
    print(A & B)

- **Difference**
  - Definition: Elements in A but not in B  
  - Example:
    print(A - B)

- **Symmetric Difference**
  - Definition: Non-common elements  
  - Example:
    print(A ^ B)

---
## 🔹 8. Dictionary in Python

**Definition:**  
A dictionary is a collection of key-value pairs used to store data in a structured way.

- Keys are unique  
- Values can be of any data type  
- Dictionaries are mutable (can be changed)  

---

### 🔹 Subtopics

- **Creating Dictionary**
  - Definition: A dictionary is created using curly braces `{}` with key-value pairs  
  - Example:
    student = {"name": "Navneet", "age": 20}

---

- **Accessing Values**
  - Definition: Values are accessed using their keys  
  - Example:
    print(student["name"])  # Navneet

---

- **Adding / Updating Values**
  - Definition: You can add a new key-value pair or update an existing value  
  - Example:
    student["age"] = 21   # Update  
    student["course"] = "Python"  # Add  

---

- **Removing Elements**
  - Definition: Elements can be removed using methods like `pop()`  
  - Example:
    student.pop("age")

---

- **Dictionary Methods**

  - **keys()**
    - Definition: Returns all keys present in the dictionary  
    - Example:
      print(student.keys())

  - **values()**
    - Definition: Returns all values present in the dictionary  
    - Example:
      print(student.values())

  - **items()**
    - Definition: Returns all key-value pairs as tuples  
    - Example:
      print(student.items())

---

## 💡 Key Points

- Dictionary stores data in **key-value format**  
- Keys must be **unique**  
- Easy and fast access using keys  
- Mutable (can modify data anytime)  



# 📚 Data Structures Basics (Python)

This repository demonstrates fundamental Python data structures including **Lists, Sets, and Dictionaries**. Each section includes explanations, operations, and example-based understanding.

---

# 🔹 1. Lists

## 📌 What is a List?

A **list** is an ordered, mutable collection that can store multiple items of different data types.

### Example:

```python
fruits = ["Apple", "Banana", "Orange", "Grapes"]
age = [20, 54, 57]
mixed = [1, "Hello", True, 3.14]
```

---

## 📌 Topics Covered

### 1. Creation of Lists

Lists are created using square brackets `[]`.

### 2. Indexing

Access elements using position (index starts from 0).

```python
mixed[1]  # Output: Hello
fruits[2] # Output: Orange
```

### 3. Slicing

Extract a portion of the list.

```python
fruits[1:4]  # ['Banana', 'Orange', 'Grapes']
```

### 4. Modifying Lists

#### ➤ Append (Add at end)

```python
fruits.append("Mango")
```

#### ➤ Insert (Add at specific index)

```python
fruits.insert(1, "Mango")
```

---

## 🧠 Example Use Case

Lists are useful when:

* Order matters
* You need duplicates
* You want to modify data frequently

---

# 🔹 2. Sets

## 📌 What is a Set?

A **set** is an unordered collection of **unique elements**.

### Example:

```python
set_1 = {1,2,3,4,5}
set_2 = {3,4,5,6,7}
```

---

## 📌 Topics Covered

### 1. Unique Elements

Sets automatically remove duplicates.

### 2. Set Operations

#### ➤ Union (All elements)

```python
union_set = set_1 | set_2
```

#### ➤ Intersection (Common elements)

```python
common_set = set_1 & set_2
```

#### ➤ Difference (Elements in set_1 not in set_2)

```python
difference = set_1 - set_2
```

### 3. Modifying Sets

#### ➤ Add Element

```python
union_set.add(8)
```

#### ➤ Remove Element

```python
union_set.remove(1)
```

### 4. Set Comprehension

```python
sqr_union_set = {x * 2 for x in union_set}
```

---

## 🧠 Example Use Case

Sets are useful when:

* You need **unique values only**
* Performing mathematical set operations
* Removing duplicates from data

---

# 🔹 3. Dictionaries

## 📌 What is a Dictionary?

A **dictionary** stores data in **key-value pairs**.

### Example:

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
```

---

## 📌 Topics Covered

### 1. Accessing Keys, Values, Items

```python
person.keys()   # All keys
person.values() # All values
person.items()  # Key-value pairs
```

### 2. Storing Multiple Values

```python
person = {
  "name": ["Alice", "John"],
  "age": [30, 25],
  "city": ["New York", "Dhaka"]
}
```

### 3. Accessing Specific Data

```python
person["city"]
person["age"]
```

### 4. Updating Values

```python
person["age"] = [31, 27]
```

### 5. Adding New Key

```python
person['email'] = ["alice@example.com", "john@example.com"]
```

---

## 🧠 Example Use Case

Dictionaries are useful when:

* Data has a **clear relationship (key → value)**
* Fast lookup is required
* Structured data storage

---

# 📊 Summary

| Data Structure | Ordered | Mutable | Unique Elements | Key Feature         |
| -------------- | ------- | ------- | --------------- | ------------------- |
| List           | Yes     | Yes     | No              | Index-based access  |
| Set            | No      | Yes     | Yes             | Fast set operations |
| Dictionary     | Yes     | Yes     | Keys unique     | Key-value mapping   |

---


# 📚 Condition & Branching in Python

This notebook demonstrates fundamental concepts of **conditional statements and branching** in Python. These concepts allow programs to make decisions based on different conditions.

---

# 🔹 1. Introduction to Conditional Statements

## 📌 What is Condition & Branching?

Conditionals allow your program to execute different blocks of code depending on whether a condition is **True or False**.

### Example:

```python
age = 18
if age >= 18:
    print("You are eligible to vote")
```

---

# 🔹 2. Types of Conditional Statements

## 📌 1. if Statement

Executes a block of code if the condition is True.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## 📌 2. if-else Statement

Executes one block if condition is True, otherwise another block.

```python
x = 3
if x > 5:
    print("Greater")
else:
    print("Smaller")
```

---

## 📌 3. if-elif-else Statement

Used when multiple conditions need to be checked.

```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")
```

---

# 🔹 3. Nested Conditions

## 📌 What is Nested if?

An **if statement inside another if statement**.

```python
age = 20
if age >= 18:
    if age >= 21:
        print("Eligible for everything")
    else:
        print("Only partially eligible")
```

---

# 🔹 4. Logical Operators in Conditions

## 📌 Operators Used

* `and` → Both conditions must be True
* `or` → At least one condition must be True
* `not` → Reverses the condition

### Example:

```python
age = 25
income = 50000

if age > 18 and income > 30000:
    print("Eligible for loan")
```

---

# 🔹 5. Comparison Operators

## 📌 Common Operators

* `==` Equal to
* `!=` Not equal to
* `>` Greater than
* `<` Less than
* `>=` Greater than or equal to
* `<=` Less than or equal to

### Example:

```python
x = 10
if x != 5:
    print("x is not equal to 5")
```

---

# 🔹 6. Short-hand (Ternary) Condition

## 📌 What is Ternary Operator?

A one-line conditional statement.

```python
x = 10
result = "Positive" if x > 0 else "Negative"
```

---

# 🔹 7. Practical Examples

## 📌 Example 1: Even or Odd

```python
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 📌 Example 2: Maximum of Two Numbers

```python
a = 5
b = 10

if a > b:
    print("a is greater")
else:
    print("b is greater")
```

---

# 📊 Summary

| Concept              | Description                     |
| -------------------- | ------------------------------- |
| if                   | Executes when condition is True |
| if-else              | Two possible outcomes           |
| if-elif-else         | Multiple conditions             |
| Nested if            | Condition inside condition      |
| Logical Operators    | Combine conditions              |
| Comparison Operators | Compare values                  |
| Ternary Operator     | One-line condition              |

---

# 📚 Loops in Python

This notebook covers the fundamental concept of **loops in Python**, which are used to execute a block of code repeatedly based on a condition.

---

# 🔹 1. Introduction to Loops

## 📌 What is a Loop?

A **loop** allows you to run the same block of code multiple times without writing it repeatedly.

### Example:

```python
for i in range(5):
    print(i)
```

---

# 🔹 2. Types of Loops

## 📌 1. for Loop

Used to iterate over a sequence (list, string, range, etc.)

```python
for i in range(1, 6):
    print(i)
```

### 🧠 Use Case

* When number of iterations is known
* Iterating through collections

---

## 📌 2. while Loop

Executes as long as a condition is True.

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

### 🧠 Use Case

* When number of iterations is unknown
* Condition-based repetition

---

# 🔹 3. Loop Control Statements

## 📌 1. break

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 📌 2. continue

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 📌 3. pass

Does nothing (placeholder for future code).

```python
for i in range(3):
    pass
```

---

# 🔹 4. Nested Loops

## 📌 What is Nested Loop?

A loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

### 🧠 Use Case

* Working with matrices
* Pattern printing

---

# 🔹 5. Loop with else

## 📌 What is loop else?

The `else` block executes when the loop completes normally (not terminated by break).

```python
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

---

# 🔹 6. Practical Examples

## 📌 Example 1: Sum of Numbers

```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

## 📌 Example 2: Multiplication Table

```python
num = 5
for i in range(1, 11):
    print(num * i)
```

---

# 📊 Summary

| Concept     | Description             |
| ----------- | ----------------------- |
| for loop    | Iterates over sequence  |
| while loop  | Runs based on condition |
| break       | Stops loop              |
| continue    | Skips iteration         |
| pass        | Placeholder             |
| Nested loop | Loop inside loop        |
| loop else   | Runs after loop ends    |

---
# 📚 Functions in Python

This notebook covers the concept of **functions in Python**, which help organize code into reusable and modular blocks.

---

# 🔹 1. Introduction to Functions

## 📌 What is a Function?

A **function** is a block of code that performs a specific task and can be reused whenever needed.

### Example:

```python
def greet():
    print("Hello, World!")

greet()
```

---

# 🔹 2. Function with Parameters

## 📌 What are Parameters?

Parameters allow you to pass data into a function.

```python
def greet(name):
    print("Hello", name)

greet("Alice")
```

---

# 🔹 3. Function with Return Value

## 📌 What is Return?

The `return` statement sends a result back to the caller.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

---

# 🔹 4. Default Parameters

## 📌 What are Default Arguments?

You can assign default values to parameters.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("John")
```

---

# 🔹 5. Keyword Arguments

## 📌 What are Keyword Arguments?

You can pass arguments using parameter names.

```python
def info(name, age):
    print(name, age)

info(age=25, name="Alice")
```

---

# 🔹 6. Variable-Length Arguments

## 📌 *args and **kwargs

Used when number of arguments is unknown.

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))
```

```python
def print_info(**data):
    print(data)

print_info(name="Alice", age=25)
```

---

# 🔹 7. Lambda Functions

## 📌 What is Lambda?

A **lambda function** is a small anonymous function.

```python
square = lambda x: x * x
print(square(5))
```

---

# 🔹 8. Recursion

## 📌 What is Recursion?

A function calling itself.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

---

# 🔹 9. Scope of Variables

## 📌 Local vs Global Scope

* Local → inside function
* Global → outside function

```python
x = 10

def show():
    x = 5
    print(x)

show()
print(x)
```

---

# 🔹 10. Practical Examples

## 📌 Example 1: Even or Odd

```python
def is_even(num):
    return num % 2 == 0

print(is_even(4))
```

## 📌 Example 2: Maximum Number

```python
def max_num(a, b):
    return a if a > b else b

print(max_num(5, 10))
```

---

# 📊 Summary

| Concept        | Description            |
| -------------- | ---------------------- |
| Function       | Reusable block of code |
| Parameters     | Input to function      |
| Return         | Output from function   |
| Default Args   | Predefined values      |
| Keyword Args   | Named arguments        |
| *args/**kwargs | Multiple inputs        |
| Lambda         | Anonymous function     |
| Recursion      | Self-calling function  |
| Scope          | Variable visibility    |

---
# 📚 Classes and Objects in Python

This notebook covers the core concept of **Object-Oriented Programming (OOP)** in Python using classes and objects. These concepts help in organizing code into reusable and structured components.

---

# 🔹 1. Introduction to Classes and Objects

## 📌 What is a Class?

A **class** is a blueprint for creating objects. It defines properties (variables) and behaviors (methods).

## 📌 What is an Object?

An **object** is an instance of a class.

### Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
print(p1.name)
```

---

# 🔹 2. The **init** Method (Constructor)

## 📌 What is **init**?

The `__init__` method is a special function that is automatically called when an object is created.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota", "Camry")
```

---

# 🔹 3. Instance Variables

## 📌 What are Instance Variables?

Variables that belong to the object.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 🔹 4. Methods in Class

## 📌 What are Methods?

Functions defined inside a class.

```python
class Dog:
    def bark(self):
        print("Woof!")

obj = Dog()
obj.bark()
```

---

# 🔹 5. self Keyword

## 📌 What is self?

Represents the current instance of the class.

```python
class Test:
    def show(self):
        print("This is self example")
```

---

# 🔹 6. Class vs Object

| Class             | Object             |
| ----------------- | ------------------ |
| Blueprint         | Instance           |
| Defines structure | Uses the structure |

---

# 🔹 7. Encapsulation

## 📌 What is Encapsulation?

Wrapping data and methods together.

```python
class Bank:
    def __init__(self, balance):
        self.balance = balance
```

---

# 🔹 8. Inheritance

## 📌 What is Inheritance?

One class can inherit properties of another class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

obj = Dog()
obj.speak()
```

---

# 🔹 9. Polymorphism

## 📌 What is Polymorphism?

Same method name behaving differently.

```python
class Bird:
    def sound(self):
        print("Bird sound")

class Cat:
    def sound(self):
        print("Meow")
```

---

# 🔹 10. Practical Example

## 📌 Example: Student Class

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s1 = Student("Alice", 90)
s1.display()
```

---

# 📊 Summary

| Concept       | Description                     |
| ------------- | ------------------------------- |
| Class         | Blueprint for objects           |
| Object        | Instance of class               |
| **init**      | Constructor method              |
| self          | Refers to current object        |
| Method        | Function inside class           |
| Encapsulation | Data + methods together         |
| Inheritance   | Reuse properties                |
| Polymorphism  | Same method, different behavior |

---

## 📂 Files Included

- `type_conversion.py` → Type conversion examples  
- `string_operations.py` → String operations  
- `tuples_and_list.py` → List & Tuple concepts  
- `sets.py` → Set concepts  
- `dictionaries.py` → Contains dictionary concepts with examples
- - `data_structures.ipynb` → 
  Includes fundamental Python data structures:
  - Lists (indexing, slicing, append, insert)
  - Sets (union, intersection, difference, uniqueness)
  - Dictionaries (key-value pairs, update, access methods)
  Each topic is explained with examples.
- `condition_branching.ipynb` → Demonstrates Python condition and branching concepts including if-else statements, nested conditions, logical operators, and real-world examples
- - `loops.ipynb` → Demonstrates loop concepts in Python including for, while, nested loops, and loop control statements with practical examples
- - `functions.ipynb` → Demonstrates Python function concepts including parameters, return statements, lambda functions, recursion, and variable scope with practical examples
 - - `class_object.ipynb` → Demonstrates Object-Oriented Programming in Python including classes, objects, methods, inheritance, and polymorphism with practical examples
---

## 🎯 Purpose

This repository is created to practice and strengthen Python fundamentals.

---

## 👤 Author

**Navneet Pal**
