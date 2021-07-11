
def stringcompression(s):
    new = []
    i = 0
    count = 1
    curr_char = ''
    while (i<len(s)):
        if i==0 or curr_char == '':
            curr_char = s[i]
            i+=1
        elif s[i] == curr_char:
            count += 1
            i+=1
        else:
            new.append(curr_char)
            new.append(str(count))
            count = 0
            curr_char = ''
            i+=1

    new_string = ''.join(new)

    if len(new_string) > len(s):
        return s
    else:
        return new_string


def stringcompression2(string):
    new = []
    i = 0
    curr_char = ''
    count = 0
    for char in string:
        if curr_char == '':
            curr_char = char
            count += 1
        elif curr_char == char:
            count += 1
        elif curr_char != char and curr_char != '':
            new.append(str(curr_char))
            new.append(str(count))
            curr_char = char
            count = 1

    new.append(str(curr_char))
    new.append(str(count))

    comp_string = ''.join(new)

    if len(comp_string) > len(string):
        return string
    else:
        return comp_string


print("stringcompression('aabcccccaaa')",stringcompression2('aabcccccaaa'))
