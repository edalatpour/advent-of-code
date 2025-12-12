# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip()

def is_invalid_id(num):
    """
    Check if a number is invalid (made of a sequence repeated exactly twice).
    Examples: 11 (1 twice), 6464 (64 twice), 123123 (123 twice)
    """
    num_str = str(num)
    length = len(num_str)
    
    # Number must have even length to be repeated twice
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    
    # Must not have leading zeros (e.g., 0101 is not valid)
    if first_half[0] == '0':
        return False
    
    return first_half == second_half

# Parse the ranges from input
ranges = input_data.split(',')

total_sum = 0

# Process each range
for range_str in ranges:
    range_str = range_str.strip()
    if not range_str:
        continue
    
    # Parse start and end of range
    start, end = map(int, range_str.split('-'))
    
    # Check each number in the range
    for num in range(start, end + 1):
        if is_invalid_id(num):
            total_sum += num

print(f"Part 1 - Sum of all invalid IDs: {total_sum}")
