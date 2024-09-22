# Initialize a variable to store the sum
mysum = 0

# Loop through numbers from 5 to 10 (inclusive) with a step of 2
for i in range(5, 11, 2):
    mysum += i  # Add the current number to mysum

    # If the sum equals 5, break out of the loop
    if mysum == 5:
        break

# Print the final value of mysum
print(mysum)
