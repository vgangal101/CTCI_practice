import os
import sys


# build a linked list 

# step 1 - compute key hash code 

# step 2 - map hash code to index in array 

# step 3 - at index store key and value

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList: 
    def __init__(self)
        self.headval = None

def init_hashtable_arr(size=10):
    hashtable_arr = []
    for i in range(size):
        hashtable_arr.append(LinkedList())
        hashtable_arr[i].headval = Node(None)
    return hashtable_arr

# remember at each position in array have a linked list 
hash_table_array = init_hashtable_arr()


def hash_function(key):
    if type(key) = int
        return key 
    else if type(key) == str
        sum = 0 
        for c in key:
            sum += ord(c)
        return sum

def add_kv_pair_to_table(key,value):
    hash_value = hash_function(key)

    index_arr = hash_value % len(hash_table_array)

    curr_node = hash_table_array[index_arr]

    if(curr_node.value == None)
        curr_node.value = value
        curr_node.next = Node(None)
    else:
        print("Error invalid operation")

    return 

def retreive_kv_pair_from_table():
    hash_value = hash_function(key)

    index_arr = hash_value % len(hash_table_array)

    curr_node = hash_table_array[index_arr]

    return 

def display_contents_of_table():

def main():
    print('hello world')
    return 



if __name__ == '__main__':
    main()

