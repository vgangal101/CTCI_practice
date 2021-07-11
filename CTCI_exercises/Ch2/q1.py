def remove_dups(LinkedList):
    head_node = LinkedList.head
    ptrFirst = head_node
    ptrSec = None

    hash_table = {}

    while(ptrFirst.next != None):
        data  = ptrFirst.data

        if data not in hash_table.keys():
            hash_table[data] = 1
        elif hash_table[data] == 1:
            ptrFirst = ptrFrist.next
            ptrSec.next = ptrFirst
        else:
            ptrSec = ptrFirst
            ptrFirst = ptrFirst.next
