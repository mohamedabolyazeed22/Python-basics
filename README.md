# **Python Documentation**

---

## *Variables and Data Types*

Built-in Data Types
 - Integers: int (e.g., x = 5)
 - Floats: float (e.g., x = 3.14)
 - Strings: str (e.g., x = "hello")
 - Boolean: bool (e.g., x = True)
 - List: list (e.g., x = [1, 2, 3])
 - Tuple: tuple (e.g., x = (1, 2, 3))
 - Dictionary: dict (e.g., x = {"name": "John", "age": 30})
 - Set: set (e.g., x = {1, 2, 3})
 - 
User-Defined Data Types
 - Classes: Define custom classes using the class keyword
 - Objects: Create objects from classes using the () operator

##**Operators**

Arithmetic Operators
 - + (addition)
 - - (subtraction)
 - * (multiplication)
 - / (division)
 - % (modulus)
 - ** (exponentiation)
  
Comparison Operators
 - == (equal to)
 - != (not equal to)
 - > (greater than)
 - < (less than)
 - >= (greater than or equal to)
 - <= (less than or equal to)
 - 
Logical Operators
 - and (logical and)
 - or (logical or)
 - not (logical not)

Assignment Operators
 - = (assignment)
 - += (addition assignment)
 - -= (subtraction assignment)
 - *= (multiplication assignment)
 - /= (division assignment)
 - %= (modulus assignment)
 - **= (exponentiation assignment)

##**Control Structures**

Conditional Statements
 - If-Else Statements:

```cpp

x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

```

If-Elif-Else Statements:

```cpp

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

```

Loops
 - For Loops:

```cpp

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

---

# **Functions**
Defining Functions
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

Lambda Functions
  - Lambda Syntax:

```cpp

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

```

---

# **Modules**

Importing Modules
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

  - Creating a Module:

```cpp

# mymodule.py
def greet(name):
    print("Hello, " + name + "!")

# main.py
import mymodule
mymodule.greet("John")  # Output: Hello, John!

```

## **File Input/Output**

---

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
