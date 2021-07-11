from collections import Counter

def isPermutation(s1,s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    return s1_counter == s2_counter

def isPermutation2(s1,s2):
    s1_dict = {}
    s2_dict = {}

    for s in s1:
        if s not in s1_dict.keys():
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1

    for s in s2:
        if s not in s2_dict.keys():
            s2_dict[s] = 1
        else:
            s2_dict[s] += 1

    return s1_dict == s2_dict

def isPermutation3(s1,s2):
    s1_dict = {}
    s2_dict = {}

    for s in s1:
        if s not in s1_dict.keys():
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1

    for s in s2:
        if s not in s2_dict.keys():
            s2_dict[s] = 1
        else:
            s2_dict[s] += 1

    isPermutation = True

    for k in s1_dict.keys():
        if k not in s2_dict.keys():
            return False
        if s1_dict[k] != s2_dict[k]:
            return False

    return isPermutation


print(isPermutation('tact coa', 'taco cat'))
print(isPermutation('Sarah','Hannah'))


print(isPermutation2('tact coa', 'taco cat'))
print(isPermutation2('Sarah','Hannah'))


print("I made it here")
print('Perm3=',isPermutation3('tact coa', 'taco cat'))
print('Perm3=',isPermutation3('Sarah','Hannah'))
