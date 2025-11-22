# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip()

# Part 1: Calculate final floor
floor = 0
for char in input_data:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(f"Part 1 - Final floor: {floor}")

# Part 2: Find position where Santa first enters basement (floor -1)
floor = 0
basement_position = None
for position, char in enumerate(input_data, start=1):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    
    # Check if Santa entered the basement for the first time
    if floor == -1 and basement_position is None:
        basement_position = position
        break

print(f"Part 2 - First basement position: {basement_position}")
