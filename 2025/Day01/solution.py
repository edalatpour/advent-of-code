# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

# Part 1: Count how many times the dial points at 0
# The dial starts at 50 and has numbers 0-99 (wraps around)
current_position = 50
zero_count = 0

# Process each rotation
for rotation in input_data:
    direction = rotation[0]  # 'L' or 'R'
    distance = int(rotation[1:])  # The number after the direction
    
    # Apply the rotation
    if direction == 'L':
        # Left means toward lower numbers (subtract)
        current_position = (current_position - distance) % 100
    else:  # direction == 'R'
        # Right means toward higher numbers (add)
        current_position = (current_position + distance) % 100
    
    # Check if we're at 0 after this rotation
    if current_position == 0:
        zero_count += 1

print(f"Part 1 - Number of times dial points at 0: {zero_count}")
