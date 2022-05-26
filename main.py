# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    word_list = list(word)
    word_list.sort()
    check_list = list(anagram)
    check_list.sort()

    correctAnagram = word_list == check_list
    return correctAnagram
    

print(find_anagrams("below", "elbow"))
print(find_anagrams("hello", "check"))
