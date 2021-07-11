from collections import Counter

def OneAway(s1,s2):
    if len(s1) > len(s2):
        # can this block be written better?
        for i in range(len(s1)):
            # does this condition break the loop ?
            if i <= len(s2):
                if s1[i] != s2[i]:
                    # check if before or after --- YOU DO NOT NEED TO CHECK THIS,
                    # THE FACT THAT THEY ARE DIFFERENT IS ENOUGH !!!!
                    if s1[i] == s2[i+1] or s1[i] == s2[i-1]:
                        return True
                else:
                    return True
            else:
                return True

    elif len(s2) > len(s1):
        # actually not bad , just put this inside a method for readibility
        # and
        for i in range(len(s2)):
            if i <= len(s2):
                if s1[i] != s2[i]:
                    # YOU DO NOT NEED TO CHECK THIS,
                    # THE FACT THAT THEY ARE DIFFERENT IS ENOUGH !!
                    if s1[i] == s2[i+1] or s1[i] == s2[i-1]:
                        return True
                else:
                    return True
            else:
                return True
    elif len(s2) == len(s1):
        #print("input are ", 's1=',s1, ' s2=', s2)
        #print("activated equals case")

        # this part is written well
        num_changes = 0
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                num_changes += 1

        #print("num_changes=",num_changes)
        if num_changes > 1:
            return False
        elif num_changes == 1:
            return True
        else:
            return False

def OneAway_revised(s1,s2):




print("OneAway('pale','ple')=",OneAway('pale','ple'))
print("OneAway('pales','pale')=",OneAway('pale','ple'))
print("OneAway('pale','bale')=",OneAway('pale','bale'))
print("OneAway('pale','bake')=",OneAway('pale','bake'))
