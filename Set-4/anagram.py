
# Check String is anagram or not 

a, b = "cinema", "iceman"


def is_anagram(str1,str2) : 
    return sorted(str1) == sorted(str2)

print(is_anagram(a, b))

