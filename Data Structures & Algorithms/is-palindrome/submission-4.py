class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_text = "".join(char.lower() for char in s if char.isalnum())

        print(clean_text)

        start = 0
        end = len(clean_text) - 1

        while start < end:
            if clean_text[start] != clean_text[end]:

                print(clean_text[start], clean_text[end])
                return False

            if start + 1 == end or start == end:
                return True

            start += 1
            end -= 1

        return True