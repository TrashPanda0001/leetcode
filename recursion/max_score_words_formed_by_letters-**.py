class Solution(object):
    # Recursive function to calculate the maximum score
    def getScore(self, words, index, score, freq_map):
        # Base case: if we've processed all words
        if index == len(words):
            return 0

        # Case 1: Do not pick the current word
        do_not_pick = 0 + self.getScore(words, index + 1, score, freq_map)

        # Case 2: Try to pick the current word
        word = words[index]
        can_make_word = True
        pick_score = 0

        # Check if we can form the word using available letters and calculate its score
        for character in word:
            # Calculate score for the character
            pick_score += score[ord(character) - ord('a')]  # ord('a') is subtracted to index the score array

            # Check if we have enough of the current character
            if freq_map.get(character, 0) == 0:
                can_make_word = False

            # "Use" the letter
            freq_map[character] = freq_map.get(character, 0) - 1

        # If we can form the word, calculate the total score including this word
        if can_make_word:
            pick = pick_score + self.getScore(words, index + 1, score, freq_map)
        else:
            pick = 0  # Cannot form the word, so the score is 0

        # Revert the changes to the frequency map (backtracking)
        for character in word:
            freq_map[character] = freq_map.get(character, 0) + 1

        # Return the maximum score of picking or not picking the word
        return max(pick, do_not_pick)

    # Main function to compute the maximum score for given words and letters
    def maxScoreWords(self, words, letters, score):
        best_score = -float('inf')  # Initialize with a very small number to find the maximum
        freq_map = {}

        # Create a frequency map for the available letters
        for letter in letters:
            freq_map[letter] = freq_map.get(letter, 0) + 1  # Increment the count for each letter

        # Start the recursion from the first word and index 0
        return self.getScore(words, 0, score, freq_map)
