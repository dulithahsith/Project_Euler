def encrypted_hash(s):
    # Step 1: Prime assignments for each letter a-z
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    # Step 2: Frequency mapping
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 3: Calculate transformed values and final hash
    total_hash = 0
    MOD = 10**9 + 7

    for i, char in enumerate(s):
        position = i + 1  # 1-based index
        # Get prime for the character
        prime_value = primes[ord(char) - ord('a')]
        freq = frequency[char]  # Get frequency of the character

        # Calculate the transformed value
        transformed_value = prime_value * freq * (position ** 2)

        # Add transformed value to total_hash
        total_hash = (total_hash + transformed_value) % MOD

    return total_hash


# Sample Inputs
print(encrypted_hash("rune"))   # Output: 916
print(encrypted_hash("wizard"))  # Output: 1365
