# Read the input from 2015/Day01/input.txt and store it in a variable
with open('2015/Day01/input.txt', 'r') as file:
    input_data = file.read().strip()

# Initialize a variable floor to 0
floor = 0

# Iterate through each character in the input string and update the floor variable accordingly
for char in input_data:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

# Print the final value of the floor variable
print(floor)
