class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}" : "{", "]":"[", ")":"("}
        list = []

        if len(s) < 2:
            return False

        for char in s:
            if char in pairs:
                if not list:
                    return False

                if list[-1] == pairs[char]:
                    list.pop()
                    continue
                else:
                    return False
            list.append(char)
        if not list:
            return True
        else:
            return False                   

        