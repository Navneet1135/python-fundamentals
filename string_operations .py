# Various String Operations in Python

# Problem 1: Extract the fourth character
text = "PYTHON"
print(text[3])  # Output: H

# Problem 2: Extract second-to-last character using negative indexing
print(text[-2])  # Output: O

# Problem 3: Extract substring "THON"
print(text[2:6])  # Output: THON

# Problem 4: Extract every second character
print(text[0:6:2])  # Output: PTO

# Problem 5: Find length of string
text2 = "Hello, World!"
print(len(text2))  # Output: 13

# Problem 6: Combine two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Output: Hello World

# Problem 7: Escape sequences
print("Hello\n\tworld")

# Problem 8: Convert to uppercase and lowercase
word = "Python Programming"
print(word.upper())
print(word.lower())

# Problem 9: Replace word
sentence = "I Love Python."
new_sentence = sentence.replace("Python", "Java")
print(new_sentence)  # Output: I Love Java.
