class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        len_digits = len(digits)
        result = []

        def comb_digits(string, idx):
            if len(string) == len(digits):
                result.append(string)
                return
            num_digits = ord(digits[idx]) - 48
            alpha_range = 3
            if (num_digits == 7) | (num_digits == 9):
                alpha_range = 4
            for i in range(alpha_range):
                small_letter = 97
                if (num_digits == 8) | (num_digits == 9):
                    small_letter = 98
                char = chr(small_letter + i + (num_digits - 2) * 3)
                comb_digits(string + char, idx + 1)

        if len_digits != 0:
            comb_digits("", 0)
        return(result)
