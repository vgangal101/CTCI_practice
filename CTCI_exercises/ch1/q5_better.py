# a better solution

def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)  # noqa
    return False


def one_edit_replace(s1, s2):
    edited = False
    i=0
    for c1, c2 in zip(s1, s2):
        #print("c1=",c1,"c2=",c2,'i=',i)
        if c1 != c2:
        #    print("c1=",c1,"c2=",c2)
            if edited:
                return False
            edited = True
        i+=1
    return True

def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

def one_edit_insert2(s1, s2):
    i = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            return False
        else:
            i += 1
    return True




print(one_edit_replace("pale","ple"))
