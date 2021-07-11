class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversal(head):
    currNode = head
    while currNode is not None:
        print(currNode.data)
        currNode = currNode.next

def prepend_node(head,item):
    newNode = ListNode(item)
    newNode.next = head
    head = newNode
    return head


def unorderedSearch(head,target):
    curNode = head
    # test
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None

def remove(head,target):
    currNode = head
    prevNode = head

    if currNode.data == target:
        head = head.next
    else:
        while(currNode is not None and currNode.data!=target):
            prevNode = currNode
            currNode = currNode.next

    print("val of prevNode",prevNode.data)
    print("val of currNode",currNode.data)

    if currNode.next is not None:
        print(currNode.next.data)
        prevNode.next = currNode.next
    else:
        prevNode.next = None

    return head

values = [2,52,18,36,13]
def generate_linked_list(values):
    currNode = ListNode(values[0])
    head_node = currNode
    for i,val in enumerate(values):
        if i == 0:
            pass
        else:
            currNode.next = ListNode(val)
            currNode = currNode.next
    return head_node

def sortedSearch(head, target):
    curNode = head
    # terminate loop if we encounter a value larger than target , early termination
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            return True
        else:
            curNode = node.next
    return False

def insert_into_sortedll(head,value):
    predNode = None
    curNode = head
    # the additional condition is because:
    while curNode is not None and value > curNode.data:
        predNode = curNode
        curNode = curNode.next
        # Link the new node into the list.
    newNode = ListNode(value)
    newNode.next = curNode
    if curNode is head:
        head = newNode
    else:
        predNode.next = newNode
    return head


def sort_linked_list(head):
    prevNode = None
    currNode = head

    while(currNode is not None):
        # in ascending order
        if  prevNode == None:
            prevNode = currNode
            currNode = currNode.next
            pass

        if prevNode.data > currNode.data:
            prevNode.next = currNode.next
            currNode.next = prevNode

        else:
            prevNode = currNode
            currNode = currNode.next

#head_node = ListNode(2)
#head_node.next = ListNode(52)
#head_node.next.next = ListNode(18)
#head_node.next.next.next = ListNode(36)
#head_node.next.next.next.next = ListNode(13)

#traversal(head_node)


#gen_linked_list = generate_linked_list(values)
#traversal(gen_linked_list)
#out = unorderedSearch(gen_linked_list,-5)
#print("output=",out)
#new_head = prepend_node(gen_linked_list,96)
#print()
#traversal(new_head)

#traversal(gen_linked_list)
#print()
#new_head2 = remove(gen_linked_list,18)
#print()
#traversal(new_head2)

#print()
#sorted_list = sort_linked_list(gen_linked_list)
#traversal

new_head = generate_linked_list([2,4,10,18,20,22])
traversal(new_head)
print()
insert_into_sortedll(new_head,19)
traversal(new_head)
