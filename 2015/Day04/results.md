# Day 4: The Ideal Stocking Stuffer - Results

## Part 1
**Question**: What is the lowest positive number that produces an MD5 hash starting with at least five zeroes when combined with the secret key?

**Answer**: 254575

### Solution Approach
- Read the secret key from input.txt: `bgvyzdsv`
- Starting from 1, incrementally test each positive number
- For each number, concatenate it with the secret key (e.g., `bgvyzdsv1`, `bgvyzdsv2`, etc.)
- Calculate the MD5 hash of the combined string
- Check if the hash starts with five zeroes (`00000`)
- Return the first number that produces such a hash

### Verification
- Input: `bgvyzdsv254575`
- MD5 Hash: `000004b30d481662b9cb0c105f6549b2`
- The hash starts with five zeroes ✓

### Verification with Examples
- `abcdef609043` → `000001dbbfa...` (expected: 609043) ✓
- `pqrstuv1048970` → `000006136ef...` (expected: 1048970) ✓
