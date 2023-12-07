class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print list function. 
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self, value):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            pop_value = value
            self.remove(value)
            return pop_value
        # else:
        #     temp = self.head
        #     while temp.next != self.tail:
        #         temp = temp.next
        #     temp.next = None
        #     self.tail = temp
        #     self.length -= 1
        #     return temp



# my_linked_list = LinkedList(4)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)

my_linked_list = LinkedList.(1)

# my_linked_list = LinkedList(1)

# my_linked_list.append(2)

# my_linked_list.print_list()

my_linked_list.pop(1)