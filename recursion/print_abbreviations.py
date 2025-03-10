# List to store all possible abbreviations
abbreviations = []

# Function to generate abbreviations
def getAbbreviations(s, index, abbreviation, skipped_count):
    # If we've reached the end of the string
    if index == len(s):
        # If there were characters skipped (skipped_count > 0), append the count at the end of the abbreviation
        if skipped_count != 0:
            abbreviation = abbreviation + str(skipped_count)
        # Append the final abbreviation to the list
        abbreviations.append(abbreviation)
        return

    # If there are skipped characters, add the skipped count to the abbreviation and continue recursively
    if skipped_count != 0:
        getAbbreviations(s, index + 1, abbreviation + str(skipped_count) + s[index], 0)
    else:
        # Otherwise, continue the abbreviation with the current character and recurse
        getAbbreviations(s, index + 1, abbreviation + s[index], 0)

    # Optionally skip the current character by incrementing the skipped_count
    getAbbreviations(s, index + 1, abbreviation, skipped_count + 1)

# Input string from user
s = input("Please enter a string: ")

# Call the function starting from index 0 with an empty abbreviation and skipped_count as 0
getAbbreviations(s, 0, "", 0)

# Print the list of abbreviations generated
print(abbreviations)


#Description:
# This program generates all possible abbreviations of a given string. The abbreviation process works by either including the character from the string or skipping it. When characters are skipped, the program counts how many characters have been skipped and represents the count in the abbreviation.
#
# Function Breakdown:
# Parameters:
#
# s: The input string for which abbreviations are to be generated.
# index: The current position in the string that the function is processing.
# abbreviation: The current state of the abbreviation being constructed.
# skipped_count: The count of characters that have been skipped so far.
# Base case (when index == len(s)):
#
# When we reach the end of the string, if any characters were skipped (skipped_count != 0), we append the count to the abbreviation.
# Then, we add the completed abbreviation to the abbreviations list.
# Recursive logic:
#
# If we have skipped characters (skipped_count != 0), we recursively add the skipped count and the current character.
# Otherwise, we either add the current character to the abbreviation or skip it by incrementing skipped_count.
# Example:
# For the input string "word", the program generates the following abbreviations:
#
# ["word", "1ord", "w1rd", "w2rd", "wo1d", "w1d", "w3d", "wo2"]
# Each abbreviation is a unique combination of keeping characters and skipping them (represented by numbers).