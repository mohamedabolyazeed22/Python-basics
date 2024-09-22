# This is our global variable 'x', available throughout the entire script.
x = 10  

def outer_function():
    # 'y' is a local variable inside 'outer_function', not accessible outside of it.
    y = 20  
    
    def inner_function():
        # 'z' is a local variable within 'inner_function'.
        z = 30 
        
        # Accessing 'x' from the global scope, 'y' from the outer scope, and 'z' from the local scope.
        print(f"x (global): {x}, y (outer): {y}, z (local): {z}")
        
    inner_function()
    
    # Trying to print 'z' here would result in an error because 'z' is not accessible outside 'inner_function'.
    # Uncommenting the next line would cause an error:
    # print(z)  # This will raise a NameError

# Call the 'outer_function', which in turn calls 'inner_function'.
outer_function()

# 'y' is not accessible here either, since it is local to 'outer_function'.
# Uncommenting the next line would cause an error:
# print(y)  # This will raise a NameError

# We can still access 'x' globally here.
print(f"x (global, outside functions): {x}")
