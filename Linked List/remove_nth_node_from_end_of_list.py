# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def remove_nth_from_end(head, n):
    curr = head
    length, ind = 0, 0

    while curr:
        curr = curr.next
        length += 1

    if length == n: return head.next

    curr = head
    while curr:
        ind += 1
        if n == length - ind:
            curr.next = curr.next.next
        curr = curr.next

    return head
