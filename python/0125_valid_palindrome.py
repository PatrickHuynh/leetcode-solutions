class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        test_word = ""
        for char in s.lower():
            test_word += char if char in alphabet else ""
        word_len = len(test_word)
        if word_len == 0:
            return True
        for i in range(0, word_len):
            x = test_word[i]
            y = test_word[-1-i]
            if (x != y):
                return False
            if (i > (word_len - 1 - i)):
                break
        return True