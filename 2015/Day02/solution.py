# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

# Part 1: Calculate total wrapping paper needed
total_paper = 0

for line in input_data:
    # Parse dimensions (format: LxWxH)
    dimensions = list(map(int, line.split('x')))
    l, w, h = dimensions[0], dimensions[1], dimensions[2]
    
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
