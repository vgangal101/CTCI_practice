import os
import sys


# build a linked list 

# step 1 - compute key hash code 

# step 2 - map hash code to index in array 

# step 3 - at index store key and value

def atoi(s):
    res = 0
    for i in range(len(s)):
        res = res * 10 + (ord(s[i]) - ord('0'))

    return res

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList: 
    def __init__(self):
        self.headval = None


class HashTable:
    def __init__(self,size):
        self.hash_table_arr = []
        self.size = size
        for i in range(size):
            self.hash_table_arr.append(None)

    def hash_function(self,key):
        if isinstance(key,int):
            return key 
        elif isinstance(key,str):
            return atoi(key)

    def add(self,key,value):
        hash_value = self.hash_function(key)        
       # print('hash value = ', hash_value)        
        index_arr = hash_value % len(self.hash_table_arr)
       # print('index arr=',index_arr)
                
        if(self.hash_table_arr[index_arr] == None):
            self.hash_table_arr[index_arr] = Node(value)
            self.hash_table_arr[index_arr].next = None
        else:
            self.hash_table_arr[index_arr].next = Node(value)

        return 

    def retrieve(self,key):
        hash_value = self.hash_function(key)
        #print('hash value = ', hash_value)
        index_arr = hash_value % len(self.hash_table_arr)
        #print('index arr=',index_arr)
        curr_node = self.hash_table_arr[index_arr]

        return curr_node.value


        
def main():
    s = 'hello world'
    ht = HashTable(10)

    ht.add('hello','world')

    result = ht.retrieve('hello')

    #print('retreived the result = ',result)
    return 



if __name__ == '__main__':
    main()

