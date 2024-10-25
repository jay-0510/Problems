class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to map characters from s to t and vice versa
        s_to_t = {}
        t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # Check if there is a conflict in the mappings
            if (c1 in s_to_t and s_to_t[c1] != c2) or (c2 in t_to_s and t_to_s[c2] != c1):
                return False
            
            # Establish the mapping between the characters
            s_to_t[c1] = c2
            t_to_s[c2] = c1
        
        return True