# python-fundamentals # Python Basics Practice

This repository contains beginner-level Python programs covering fundamental concepts.

## Topics Covered

### 1. Type Conversion
Examples of converting data types in Python:
- Boolean to String using `str()`
- String to Integer using `int()`
- Integer to Float using `float()`

### 2. String Operations
Basic string manipulation techniques:
- Indexing and Negative Indexing
- Slicing (`start:stop:step`)
- Finding string length using `len()`
- Concatenation using `+`
- Escape sequences (`\n`, `\t`)
- Case conversion (`upper()`, `lower()`)
- Replacing text using `replace()`


## 🔹 What is a List in Python?

A **list** is a collection used to store multiple items in a single variable.

👉 It is **ordered and mutable**, which means:
- You can access elements using index
- You can modify, add, or remove elements


  ## 🔹 What is a Tuple in Python?

A **tuple** is a collection of multiple items stored in a single variable.

- Tuples are **ordered** (items have a fixed position)
- Tuples are **immutable** (cannot be changed after creation)
- They can store different data types

### Example:
```python
numbers = (10, 20, 30)

### Example:
```python
numbers = [10, 20, 30, 40]
numbers[0] = 100  # List can be modified

# 📘 Python Lists & Tuples Notes

## 🔹 Topics Covered

### 1. Nested List Access
A list inside another list.  
We use multiple indexing to access elements.

### 2. Nested Tuple Access
Tuples can also contain tuples.  
Access works same as lists.

### 3. Negative Indexing
Negative index starts from the end.  
Example: `-1` means last element.

### 4. List Slicing with Step
Syntax: `list[start:end:step]`  
Used to extract elements with skipping.

### 5. Adding Elements (append)
`append()` adds an element at the end of list.

### 6. Removing Elements (remove)
`remove()` deletes a specific value from list.

### 7. List vs Tuple
- List → mutable (can change)
- Tuple → immutable (fixed)


## Files Included
- `type_conversion.py` → Demonstrates type conversion examples  
- `string_operations.py` → Contains string manipulation programs
- `tuples_and_list.py` → Contains list and tuple concepts with examples 

## Purpose
This repository is created to practice and strengthen Python fundamentals.

## Author
Navneet Pal
