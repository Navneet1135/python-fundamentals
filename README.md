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

## 📂 Files Included

- `type_conversion.py` → Type conversion examples  
- `string_operations.py` → String operations  
- `tuples_and_list.py` → List & Tuple concepts  
- `sets.py` → Set concepts  

---

## 🎯 Purpose

This repository is created to practice and strengthen Python fundamentals.

---

## 👤 Author

**Navneet Pal**
