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
---

## 🎯 Purpose

This repository is created to practice and strengthen Python fundamentals.

---

## 👤 Author

**Navneet Pal**
