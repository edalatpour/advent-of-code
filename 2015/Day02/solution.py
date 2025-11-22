# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

# Part 1: Calculate total wrapping paper needed
total_paper = 0

for line in input_data:
    # Skip empty lines
    if not line.strip():
        continue
    
    # Parse dimensions (format: LxWxH)
    dimensions = list(map(int, line.split('x')))
    l, w, h = dimensions
    
    # Calculate the three side areas
    side1 = l * w
    side2 = w * h
    side3 = h * l
    
    # Calculate surface area: 2*l*w + 2*w*h + 2*h*l
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    
    # Find the smallest side for slack
    smallest_side = min(side1, side2, side3)
    
    # Total paper for this present
    paper_needed = surface_area + smallest_side
    total_paper += paper_needed

print(f"Part 1 - Total wrapping paper needed: {total_paper} square feet")

# Part 2: Calculate total ribbon needed
total_ribbon = 0

for line in input_data:
    # Skip empty lines
    if not line.strip():
        continue
    
    # Parse dimensions (format: LxWxH)
    dimensions = list(map(int, line.split('x')))
    l, w, h = dimensions
    
    # Sort dimensions to easily find the two smallest
    sorted_dims = sorted([l, w, h])
    
    # Ribbon for wrapping: smallest perimeter = 2 * (smallest + second_smallest)
    wrapping_ribbon = 2 * (sorted_dims[0] + sorted_dims[1])
    
    # Ribbon for bow: volume = l * w * h
    bow_ribbon = l * w * h
    
    # Total ribbon for this present
    ribbon_needed = wrapping_ribbon + bow_ribbon
    total_ribbon += ribbon_needed

print(f"Part 2 - Total ribbon needed: {total_ribbon} feet")
