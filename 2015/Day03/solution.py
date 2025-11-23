# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip()

# Part 1: Count houses that receive at least one present
# Start at position (0, 0)
x, y = 0, 0

# Set to track all visited houses (using tuples for coordinates)
visited_houses = set()

# Deliver present to starting house
visited_houses.add((x, y))

# Process each move
for move in input_data:
    if move == '^':  # North
        y += 1
    elif move == 'v':  # South
        y -= 1
    elif move == '>':  # East
        x += 1
    elif move == '<':  # West
        x -= 1
    
    # Deliver present to current house
    visited_houses.add((x, y))

# Count unique houses that received at least one present
houses_with_presents = len(visited_houses)

print(f"Part 1 - Houses with at least one present: {houses_with_presents}")
