class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):  # <- My solution
    val1, val2 = "", ""

    curr = l1
    while curr:
        val1 = str(curr.val) + val1
        curr = curr.next

    curr = l2
    while curr:
        val2 = str(curr.val) + val2
        curr = curr.next

    sum = str(int(val1) + int(val2))

    new_head = ListNode()

    new_curr = new_head
    for i in "".join(reversed(sum)):
        new_curr.next = ListNode(int(i))
        new_curr = new_curr.next

    return new_head.next

