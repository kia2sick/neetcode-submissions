class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))+"#"+s  
        
        return encoded    

    def decode(self, s: str) -> List[str]:
        num = ""
        result = []
        i = 0
        while i < len(s):
            read = s[i]
            if read != "#":
                num += read
                i+=1
            else:
                nums = int(num)
                start = i + 1
                end = nums + start
                string = s[start:end]
                result.append(string)
                i = end
                num = ""    

        return result
