import hashlib

# Read the input from input.txt and store it in a variable
with open('input.txt', 'r') as file:
    secret_key = file.read().strip()

# Part 1: Find the lowest positive number that produces an MD5 hash starting with five zeroes
def find_adventcoin(secret_key, leading_zeroes=5):
    """
    Find the lowest positive number that, when combined with the secret key,
    produces an MD5 hash starting with the specified number of leading zeroes.
    """
    number = 1
    prefix = '0' * leading_zeroes
    
    while True:
        # Combine secret key with the current number
        test_string = f"{secret_key}{number}"
        
        # Calculate MD5 hash
        hash_result = hashlib.md5(test_string.encode()).hexdigest()
        
        # Check if hash starts with required number of zeroes
        if hash_result.startswith(prefix):
            return number
        
        number += 1

# Find the answer for Part 1
result = find_adventcoin(secret_key, leading_zeroes=5)
print(f"Part 1 - Lowest number for hash starting with five zeroes: {result}")

# Verify the hash
test_string = f"{secret_key}{result}"
hash_result = hashlib.md5(test_string.encode()).hexdigest()
print(f"Verification: {test_string} → {hash_result}")
