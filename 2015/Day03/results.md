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
