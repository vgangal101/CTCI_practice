import os
import sys

def urlify_algo(string,length):
    char_list = list(string)
    string = ""
    new_index = len(char_list)
    print('new_index=',new_index)

    for i in reversed(range(length)):
        print('i=',i)
        if char_list[i] == ' ':
            # replace spaces

            char_list[new_index - 3 : new_index] = "%20"
            new_index -=3
        else:
            #move characters
            char_list[new_index-1] = char_list[i]
            new_index -= 1

    # convert back to string
    return string.join(char_list)

if __name__  == '__main__':
    print(urlify_algo("Mr John Smith    ",13))
