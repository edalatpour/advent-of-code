--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

## Solution

The solution to the puzzle involves reading the input from a file, iterating through each character in the input string, and updating a variable `floor` accordingly. An opening parenthesis `(` increases the floor by 1, while a closing parenthesis `)` decreases the floor by 1. The final value of the `floor` variable is the answer to the puzzle.

```python
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
```
