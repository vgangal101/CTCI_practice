from collections import Counter
def isPalindromePermutation(string):
    s = string.replace(' ','')
    str_counter = Counter(s)
    count = 0
    for k in str_counter.keys():
        if str_counter[k] == 2:
            count += 1

    if count >= 2 :
        return True
    else:
        return False



print("isPalindromePermutation('taco cat')",isPalindromePermutation('taco cat'))
