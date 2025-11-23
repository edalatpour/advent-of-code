# Day 3: Perfectly Spherical Houses in a Vacuum - Results

## Part 1
**Question**: How many houses receive at least one present?

**Answer**: 2592 houses

### Solution Approach
- Started at position (0, 0) and delivered a present
- Used a set to track all unique house positions visited
- For each direction in the input:
  - `^` moves north (y + 1)
  - `v` moves south (y - 1)
  - `>` moves east (x + 1)
  - `<` moves west (x - 1)
- Delivered a present at each new position
- Counted the total number of unique houses visited

### Verification with Examples
- `>` → 2 houses ✓
- `^>v<` → 4 houses ✓
- `^v^v^v^v^v` → 2 houses ✓

## Part 2
**Question**: Santa and Robo-Santa start at the same location and take turns moving. How many houses receive at least one present?

**Answer**: 2360 houses

### Solution Approach
- Both Santa and Robo-Santa start at position (0, 0) and both deliver a present
- Used a single set to track all unique house positions visited by either Santa or Robo-Santa
- Santa takes even-indexed moves (0, 2, 4, ...)
- Robo-Santa takes odd-indexed moves (1, 3, 5, ...)
- For each character in the input, the corresponding deliverer moves and delivers a present
- Counted the total number of unique houses visited by either deliverer

### Verification with Examples
- `^v` → 3 houses (Santa goes north, Robo-Santa goes south) ✓
- `^>v<` → 3 houses (both end up back at start) ✓
- `^v^v^v^v^v` → 11 houses (Santa goes north 5 times, Robo-Santa goes south 5 times) ✓
