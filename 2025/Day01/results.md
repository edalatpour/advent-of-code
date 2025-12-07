# Day 1: Secret Entrance - Results

## Part 1
**Question**: What's the actual password to open the door (number of times the dial points at 0)?

**Answer**: 1031

### Solution Approach
- Started with the dial pointing at 50
- The dial has numbers 0-99 arranged in a circle
- For each rotation instruction:
  - `L` (left) means rotate toward lower numbers (subtract)
  - `R` (right) means rotate toward higher numbers (add)
  - Used modulo 100 to handle wrap-around
- Counted every time the dial pointed at 0 after a rotation

### Verification with Example
The example from the problem:
```
L68, L30, R48, L5, R60, L55, L1, L99, R14, L82
```

Produces the following sequence:
- Start: 50
- L68 → 82
- L30 → 52
- R48 → 0 ✓ (count: 1)
- L5 → 95
- R60 → 55
- L55 → 0 ✓ (count: 2)
- L1 → 99
- L99 → 0 ✓ (count: 3)
- R14 → 14
- L82 → 32

Expected: 3 times ✓
Our solution correctly produces 3 for this example.

### Key Insights
- The dial wraps around: moving left from 0 goes to 99, moving right from 99 goes to 0
- Python's modulo operator `%` naturally handles this circular behavior
- We only count when the dial points at 0 **after** a rotation, not at the start
