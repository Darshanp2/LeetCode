"""
242. Valid Anagram

Time Complexity: O(n)

"""

def validAnagram(self, s: str, t: str)->bool:

    dct1, dct2 = {}, {}
    for i in s:
        if i not in dct1:
            dct1[i] = 1
        else:
            dct1 += 1
    
    for j in t:
        if j not in dct2:
            dct2[j] = 1
        else:
            dct2 += 1
    
    if dct1 == dct2:
        return True
    else:
        return False
    
    