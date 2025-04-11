# O(N^2) Time | O(N) Space
def semordnilap(words):
    groups = []

    for i in range(len(words)):
        semordnilaps = [words[i]]
        for j in range(i + 1, len(words)):
            word_j = words[j]
            if words[i] == word_j[::-1]:
                semordnilaps.append(word_j)
                groups.append(semordnilaps)

    return groups

# O(N * M) Time | O(M) Space
def semordnilap(words):
    wordSet = set(words)
    groups = []
    for word in words:
        reverse = word[::-1]
        if reverse in wordSet and reverse != word:
            groups.append([word, reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)

    return groups

if __name__ == '__main__':
    words = ["diaper", "abc", "test", "cba", "repaid"]
    print(semordnilap(words))
