class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
    res = {None: None}
    curr = head

    while curr:
        res[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        curr_copy = res[curr]
        curr_copy.next = res[curr.next]
        curr_copy.random = res[curr.random]
        curr = curr.next

    return res[head]
