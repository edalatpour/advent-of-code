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

# Part 2: Santa and Robo-Santa alternate moves
# Both start at position (0, 0)
santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0

# Set to track all visited houses by both Santa and Robo-Santa
visited_houses_part2 = set()

# Both deliver present to starting house
visited_houses_part2.add((santa_x, santa_y))

# Process each move, alternating between Santa and Robo-Santa
for i, move in enumerate(input_data):
    # Santa takes even-indexed moves (0, 2, 4, ...)
    # Robo-Santa takes odd-indexed moves (1, 3, 5, ...)
    if i % 2 == 0:
        # Santa's turn
        if move == '^':  # North
            santa_y += 1
        elif move == 'v':  # South
            santa_y -= 1
        elif move == '>':  # East
            santa_x += 1
        elif move == '<':  # West
            santa_x -= 1
        
        # Deliver present to Santa's current house
        visited_houses_part2.add((santa_x, santa_y))
    else:
        # Robo-Santa's turn
        if move == '^':  # North
            robo_y += 1
        elif move == 'v':  # South
            robo_y -= 1
        elif move == '>':  # East
            robo_x += 1
        elif move == '<':  # West
            robo_x -= 1
        
        # Deliver present to Robo-Santa's current house
        visited_houses_part2.add((robo_x, robo_y))

# Count unique houses that received at least one present
houses_with_presents_part2 = len(visited_houses_part2)

print(f"Part 2 - Houses with at least one present: {houses_with_presents_part2}")
