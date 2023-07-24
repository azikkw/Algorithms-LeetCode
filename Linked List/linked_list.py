class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, d):
        self.data = d

    def set_next(self, n):
        self.next = n


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def remove_node(self, data):
        this_node = self.head
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_data())
                else:
                    self.head = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False

    def find_node(self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None

    def get_list(self):
        this_node = self.head
        linked_list = []
        while this_node:
            linked_list.append(this_node.get_data())
            this_node = this_node.get_next()
        return linked_list


my_list = LinkedList()

my_list.add_node(5)
my_list.add_node(4)
my_list.add_node(3)
my_list.add_node(1)

print(my_list.head.get_next().get_next().get_data())
print(my_list.get_list())
my_list.remove_node(4)
print(my_list.get_size())
print(my_list.find_node(4))
