# =========================================
# Python Lists & Tuples - All Topics
# =========================================

# -----------------------------------------
# 1. Nested List Access
# -----------------------------------------
nested_list = [["a", "b", "c"], [1, 2, 3], ["x", "y", "z"]]
print("1. Nested List Access:", nested_list[1][2])

# -----------------------------------------
# 2. Nested Tuple Access
# -----------------------------------------
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("2. Nested Tuple Access:", nested_tuple[1][2])

# -----------------------------------------
# 3. Negative Indexing
# -----------------------------------------
numbers = [10, 20, 30, 40, 50]
print("3. Negative Indexing:", numbers[-3:])

# -----------------------------------------
# 4. List Slicing with Step
# -----------------------------------------
numbers = [10, 20, 30, 40, 50, 60]
print("4. Slicing with Step:", numbers[1:5:2])

# -----------------------------------------
# 5. Adding Elements (append)
# -----------------------------------------
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("5. After Append:", fruits)

# -----------------------------------------
# 6. Removing Elements (remove)
# -----------------------------------------
fruits.remove("orange")
print("6. After Remove:", fruits)

# -----------------------------------------
# 7. List vs Tuple
# -----------------------------------------
list_example = [1, 2, 3]
list_example[0] = 10

tuple_example = (1, 2, 3)
# tuple_example[0] = 10  # Error

print("7. List (Mutable):", list_example)
print("7. Tuple (Immutable):", tuple_example)
