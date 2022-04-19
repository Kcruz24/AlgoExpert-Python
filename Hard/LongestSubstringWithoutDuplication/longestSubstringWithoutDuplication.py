from collections import Counter

# O(N) time | O(min(n, a)) space - Where "n" is the length of the input string
# and "a" is the length of the character alphabet represented in the input string
def longestSubstringWithoutDuplication(s):
    last_seen = {}
    longest = [0, 1]

    start_idx = 0

    for idx, char in enumerate(s):
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char] + 1)

        if longest[1] - longest[0] < idx + 1 - start_idx:
            longest = [start_idx, idx + 1]

        last_seen[char] = idx

    longest_substring = s[longest[0]: longest[1]]

    return longest_substring
