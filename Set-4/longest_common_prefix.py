
def longest_common_prefix(words):
    if not words:
        return ""

    curr = words[0]

    for word in words[1:]:
        i = 0
        while i < len(curr) and i < len(word) and curr[i] == word[i]:
            i = i + 1
        curr = curr[:i]

    return curr




arr = ["flower", "flow", "flight"]
res = longest_common_prefix(arr)
print(res) 
