class Solution():
    key_mappings = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }

    def getCombinations(self, digits, index):
        if index == len(digits):
            return [""]
        combinations_till_now = self.getCombinations(digits, index + 1)
        possibleAlphabetsForCurrentDigit = self.key_mappings[int(digits[index])]
        new_combinations = []
        for combination in combinations_till_now:
            for alphabet in possibleAlphabetsForCurrentDigit:
                new_combinations.append(alphabet + combination)
        return new_combinations

    def letterCombinations(self, digits):
        if(digits==""):
            return []
        return self.getCombinations(digits, 0)

    def __init__(self):
        digits = input("enter a string")
        print(self.letterCombinations(digits))

s = Solution()


Time Complexity