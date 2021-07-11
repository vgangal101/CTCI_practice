from collections import Counter

def isEven(n):
    return n % 2 == 0

def isPalindromePermutation(s):
    # make the frequency count
    char_frequency = Counter(s)
    odd_count = 0

    # odd_count cannot be larger than one , if so return False

    for char in char_frequency.keys():
        if isEven(char_frequency[char]):
            continue
        elif not isEven(char_frequency[char]):
            odd_count += 1

    if odd_count >  1:
        return False
    else:
        return True


def isPalindromePermutation2(s):
    # this time make the frequency tally manually

    char_frequency = {}
    odd_count = 0

    for char in s:
        if char not in char_frequency.keys():
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    #print(char_frequency)

    for char in char_frequency.keys():
        if isEven(char_frequency[char]):
            continue
        elif not isEven(char_frequency[char]):
            odd_count += 1

    if odd_count > 1:
        return False
    else:
        return True


print("isPalindromePermutation('tacocat')",isPalindromePermutation('tacocat'))
print("isPalindromePermutation2('tacocat')",isPalindromePermutation2('tacocat'))


print("isPalindromePermutation('hhnnaa')",isPalindromePermutation('hhnnaa'))
print("isPalindromePermutation2('hhnnaa')",isPalindromePermutation2('hhnnaa'))

print("isPalindromePermutation('hhnnaacz')",isPalindromePermutation('hhnnaacz'))
print("isPalindromePermutation2('hhnnaacz')",isPalindromePermutation2('hhnnaacz'))
