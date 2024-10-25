class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Calculate XOR of x and y
        xor = x ^ y
        
        # Count the number of 1s in the binary representation of xor
        distance = 0
        while xor:
            distance += xor & 1  # Check the last bit
            xor >>= 1            # Shift right to check the next bit
        return distance