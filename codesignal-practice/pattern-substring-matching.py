'''
Question
--------
You are given two strings - `pattern` and `source`. The first string `pattern` contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Let’s say that `pattern` matches a substring `source[1..r]` of source if the following three conditions are met:
* They have equal length,
* For each `0` in `pattern`, the corresponding letter in the substring is a vowel,
* For each `1` in `pattern`, the corresponding letter is a consonant

Your task is to calculate the number of substrings of `source` that match `pattern`.

Note: In this task we define the vowels as `a, e, i, o, u, y`. All other letters are consonants.

Example:

For `pattern = “010”` and `source = “amazing”`, the output should be `2`. 

a m a z i n g

0 1 0

    0 1 0
'''


def is_vowel(char, vowels):
    return char in vowels


def characters_match(pattern, source, p_index, s_index, vowels):
    return (pattern[p_index] == '0' and is_vowel(source[s_index], vowels)) or \
    (pattern[p_index] == '1' and not is_vowel(source[s_index], vowels))


def solution(pattern, source):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    matches = 0

    # for each alphabet
    for i in range(len(source) - len(pattern) + 1):
        # can a substring start
        if characters_match(pattern, source, 0, i, vowels):
            # does a substring match the pattern
            match = True
            # check the next len(pattern) characters
            for j in range(0, len(pattern)):
                # if there is a mismatch, note that and exit
                if not characters_match(pattern, source, j, i+j, vowels):
                    match = False
                    break
                # if no mismatch, then increase the counter
                if match:
                    matches += 1
    return matches
