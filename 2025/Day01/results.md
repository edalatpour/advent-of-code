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

## Part 2
**Question**: Using password method 0x434C49434B (counting all times the dial points at 0 during rotations, not just at the end), what is the password?

**Answer**: 5831

### Solution Approach
Part 2 requires counting EVERY time the dial points at 0, including:
- When it lands on 0 at the end of a rotation (Part 1)
- When it passes through 0 during a rotation

Key insights:
- For RIGHT rotation from position `p` by distance `d`:
  - We pass through 0 when we cross multiples of 100
  - If `p == 0`: count = `d // 100` (hit 0 at steps 100, 200, 300, ...)
  - If `p > 0`: first hit at step `100-p`, then every 100 steps
    - Count = `1 + ((d - (100-p)) // 100)` if `d >= 100-p`, else 0
- For LEFT rotation from position `p` by distance `d`:
  - If `p == 0`: count = `d // 100` (hit 0 at steps 100, 200, 300, ...)
  - If `p > 0`: first hit at step `p`, then every 100 steps
    - Count = `1 + ((d - p) // 100)` if `d >= p`, else 0

### Verification with Example
Using the same example as Part 1:
```
L68, L30, R48, L5, R60, L55, L1, L99, R14, L82
```

Step-by-step trace:
- Start: 50
- L68 from 50: passes through 0 once (at step 50) → 82 (count: 1)
- L30 from 82: no crossing → 52 (count: 1)
- R48 from 52: passes through 0 once (at step 48, landing at 100≡0) → 0 (count: 2)
- L5 from 0: no crossing (would need 100+ steps) → 95 (count: 2)
- R60 from 95: passes through 0 once (at step 5) → 55 (count: 3)
- L55 from 55: passes through 0 once (at step 55) → 0 (count: 4)
- L1 from 0: no crossing → 99 (count: 4)
- L99 from 99: passes through 0 once (at step 99) → 0 (count: 5)
- R14 from 0: no crossing → 14 (count: 5)
- L82 from 14: passes through 0 once (at step 14) → 32 (count: 6)

Expected: 6 times ✓
Our solution correctly produced 6 for this example.

### Key Insights
- Large rotations (like R1000) can pass through 0 multiple times: `1000 // 100 = 10` times
- The problem requires careful tracking of when we cross 0 during rotation, not just at the end
- The formula accounts for both the initial crossing and subsequent crossings every 100 steps
