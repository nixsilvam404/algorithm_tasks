from collections import Counter

def minStepsToAnagram(s, t):
    countS = Counter(s)
    countT = Counter(t)
    print(countS)
    print(countT)

    # Calculate the differences in counts
    diff = countT - countS
    print(diff)

    # Sum the differences to get the minimum number of steps
    return sum(diff.values())


print(minStepsToAnagram("bab", "aba"))
print(minStepsToAnagram("leetcode", "practice")) 
print(minStepsToAnagram("anagram", "mangaar"))