# We start by setting x to 5. This is our global variable.
x = 5 

# Define a function 'g' that takes 'y' as its parameter.
def g(y):
    # Here, we're adding the global variable x to the parameter y.
    y = y + x
    
    # Print the updated value of y.
    print(y)

# Call the function 'g' with the value of x as its argument.
g(x)

