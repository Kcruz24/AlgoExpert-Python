# O(N * M) Time | O(M) Space
def commonCharacters(strings):
    seen = {}

    for word in strings:
        word = set(word)
        for char in word:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
    print(seen)
    common_chars = []
    for key, val in seen.items():

        if val == len(strings):
            common_chars.append(key)

    return common_chars

if __name__ == '__main__':
    strings = ["abc", "bcd", "cbad"]

    print(commonCharacters(strings))

