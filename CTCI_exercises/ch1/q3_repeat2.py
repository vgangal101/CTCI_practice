import os
import sys

def URLify(string,true_len):
    s_list = list(string)
    s_list_len = len(s_list)

    for i in reversed(range(true_len)):
        if s_list[i] != ' ':
            s_list[i+1] = s_list[i]
        elif s_list[i] == ' ':
            s_list[i-2:i] = "%20"

    return ''.join(s_list)

print(URLify('Mr John Smith    ',13))
