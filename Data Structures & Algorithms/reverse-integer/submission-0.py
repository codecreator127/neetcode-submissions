class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)

        if number[0] == "-":
            num = number[1:]
            out = int("-" + num[::-1])
        else:
            out = int(number[::-1])

        if -(2**31 - 1) > out or out > (2**31 - 1):
            return 0
        
        return out