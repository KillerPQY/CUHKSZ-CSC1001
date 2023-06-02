def isAnagram(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    if sorted(l1) == sorted(l2):
        return True
    else:
        return False


s1 = input('Please enter the first string:')
s2 = input('Please enter the second string:')
if isAnagram(s1, s2):
    print('is an anagram')
else:
    print('is not an anagram')
