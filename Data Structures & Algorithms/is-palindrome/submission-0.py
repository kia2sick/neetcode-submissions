class Solution:
    def isPalindrome(self, s: str) -> bool:
         x = (len(s) - 1)
         i = 0
         while i < x:
             if not s[i].isalnum():
                   i+=1
                   continue
             if not s[x].isalnum():
                    x-=1
                    continue   
             else:
                  if s[i].lower() != s[x].lower():
                      return False
                  i +=1 
                  x -= 1    
         return True        

                

