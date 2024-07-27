class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold the mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the top element matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the current opening bracket onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been matched correctly
        return not stack

# Example usage
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("{[]}"))  # Output: True
