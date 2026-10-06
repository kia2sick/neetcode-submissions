class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for i in range(len(s)):
           
            if s[i] not in seen:
                seen.add(s[i]) 
            else:
                while s[i] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[i])

            max_length = max(len(seen), max_length)    
        
        return max_length                
