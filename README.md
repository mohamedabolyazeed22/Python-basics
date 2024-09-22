# **Welcome to Python Wonderland!**

---

## *Variables and Data Types: The Magic Ingredients*

- Built-in Data Types
  - Integers: Whole numbers, like x = 5
  - Floats: Decimal numbers, like x = 3.14
  - Strings: Sequences of characters, like x = "hello"
  - Boolean: True or False values, like x = True
  - List: Ordered collections of items, like x = [1, 2, 3]
  - Tuple: Ordered, immutable collections of items, like x = (1, 2, 3)
  - Dictionary: Key-value pairs, like x = {"name": "John", "age": 30}
  - Set: Unordered collections of unique items, like x = {1, 2, 3}
   
- User-Defined Data Types
  - Classes: Define custom classes using the class keyword
  - Objects: Create objects from classes using the () operator

##**Operators: The Magic Wands**

- Arithmetic Operators: Perform mathematical magic!
  - `+` (addition)
  - `-` (subtraction)
  - `*` (multiplication)
  - `/` (division)
  - `%` (modulus)
  - `**` (exponentiation)
  
- Comparison Operators: Compare values with ease!
  - `==` (equal to)
  - `!=` (not equal to)
  - `>` (greater than)
  - `<` (less than)
  - `>=` (greater than or equal to)
  - `<=` (less than or equal to)
 
- Logical Operators: Make logical decisions!
  - `and` (logical and)
  - `or` (logical or)
  - `not` (logical not)

- Assignment Operators: Assign values with style!
  - `=` (assignment)
  - `+=` (addition assignment)
  - `-=` (subtraction assignment)
  - `*=` (multiplication assignment)
  - `/=` (division assignment)
  - `%=` (modulus assignment)
  - `**`= (exponentiation assignment)

---

## **Control Structures: The Magic Paths: Make decisions with if-else statements!**

**Conditional Statements**

 - If-Else Statements:

```cpp

x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

```

- If-Elif-Else Statements:

```cpp

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

```

**Loops: Repeat tasks with ease!**

 - For Loops:

```cpp

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

---

# **Functions: The Magic Spells**
**Defining Functions: Create reusable code!**

  - Function Syntax:

```cpp

def greet(name):
    print("Hello, " + name + "!")

greet("John")  # Output: Hello, John!

```

  - Function Arguments:

```cpp

def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8

```

**Lambda Functions: Create small, anonymous functions!**

  - Lambda Syntax:

```cpp

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

```

---

# **Modules: The Magic Libraries**

**Importing Modules: Use pre-built code!**

 - Importing Built-in Modules:

 ```cpp
 
 import math
print(math.pi)  # Output: 3.14159265359

 ```
 
   - Importing External Modules:
 
```cpp

import requests
response = requests.get("https://www.example.com")
print(response.status_code)  # Output: 200

```

  - Creating a Module:: Create your own reusable code!

```cpp

# mymodule.py
def greet(name):
    print("Hello, " + name + "!")

# main.py
import mymodule
mymodule.greet("John")  # Output: Hello, John!

```

---

## **File Input/Output**

**Reading Files**

  - Reading a Text File:
  - 
  ```cpp
  
  with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
 ```
 
  - Reading a CSV File:

```cpp

import csv
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 
        
```

  - Writing a Text File:

```cpp

with open("example.txt", "w") as file:
    file.write("Hello, World!")
    
```

  - Writing a CSV File:
 
```cpp

import csv
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 30])
    
```
