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

# Part 2: Count how many times the dial points at 0 during rotations
# This includes both ending at 0 AND passing through 0 during rotation
# Think of it as: how many times does the dial point at a position that is 0 (mod 100)
current_position = 50
zero_count_part2 = 0

# Process each rotation
for rotation in input_data:
    direction = rotation[0]  # 'L' or 'R'
    distance = int(rotation[1:])  # The number after the direction
    
    # When rotating, we move through positions. We need to count how many times
    # we land on a position that is 0 (mod 100).
    # 
    # For RIGHT rotation from position p by distance d:
    # We go through: p+1, p+2, ..., p+d
    # We hit 0 (mod 100) when p+k ≡ 0 (mod 100), i.e., k ≡ -p (mod 100)
    # For p in [0, 99]: k = 100-p, 200-p, 300-p, ... (if p > 0)
    # Or k = 100, 200, 300, ... (if p == 0)
    # Number of such k in [1, d]: floor((d + p) / 100)
    #
    # For LEFT rotation from position p by distance d:
    # We go through: p-1, p-2, ..., p-d (thinking in terms of steps, not positions)
    # Equivalently, we visit positions: (p-1) % 100, (p-2) % 100, ..., (p-d) % 100
    # We hit 0 when p-k ≡ 0 (mod 100), i.e., k ≡ p (mod 100)
    # For p > 0: k = p, p+100, p+200, ... as long as k <= d
    # For p == 0: k = 100, 200, 300, ... as long as k <= d
    
    if direction == 'L':
        # Count how many k in [1, d] such that (p - k) % 100 == 0
        if current_position == 0:
            # k must be a multiple of 100
            zero_count_part2 += distance // 100
        else:
            # k = current_position, current_position + 100, current_position + 200, ...
            if distance >= current_position:
                zero_count_part2 += 1 + ((distance - current_position) // 100)
        current_position = (current_position - distance) % 100
    else:  # direction == 'R'
        # Count how many k in [1, d] such that (p + k) % 100 == 0
        # i.e., k ≡ -p (mod 100)
        # For p in [0, 99]: this is k = (100-p), (200-p), (300-p), ...
        # But if p == 0, then k = 100, 200, 300, ...
        if current_position == 0:
            # k must be a multiple of 100
            zero_count_part2 += distance // 100
        else:
            # k = 100-current_position, 200-current_position, ...
            # First hit is at k = 100 - current_position
            if distance >= 100 - current_position:
                zero_count_part2 += 1 + ((distance - (100 - current_position)) // 100)
        current_position = (current_position + distance) % 100

print(f"Part 2 - Number of times dial points at 0 (including during rotations): {zero_count_part2}")
