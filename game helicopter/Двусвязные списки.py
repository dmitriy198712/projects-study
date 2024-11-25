class Node(object):
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_
 
    def get_data(self):
        return self.data
 
    def get_next(self):
        return self.next_
 
    def set_data(self, data):
        self.data = data
 
    def set_next(self, next_):
        self.next_ = next_
 
 
class LinkedList(object):
    def __init__(self):
        self.head = None
 
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
 
    def show(self):
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output)
 
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)
 
    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node
 
    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)
 
    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()
 
    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')
 
    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.push_front(data)
                return
            if count + 1 == index:
                node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')
 
    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.remove_front()
                return
            if count + 1 == index:
                node_to_remove = cur_node.get_next()
                node_after_remove = node_to_remove.get_next()
                cur_node.set_next(node_after_remove)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')
 
    def reverse_(self):
        prev = None
        cur_node = self.head
        next_ = None
        while cur_node is not None:
            next_ = cur_node.get_next() # выбираем следующее
            cur_node.set_next(prev) # следующим делаем предыдущее
            prev = cur_node # предыдущее сдвигаем на текущее
            cur_node = next_ # а текущее передвигаем на следующее
        self.head = prev
 
 
my_list = LinkedList()
my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)
 
# my_list.show()
# my_list.push_front(56)
# my_list.show()
# print(my_list.value_at(2))
# my_list.length()
# my_list.show()
# my_list.remove_back()
# my_list.show()
# my_list.remove_front()
# my_list.show()
# my_list.insert(2, 15)
# my_list.show()
my_list.remove(1)
my_list.show()
my_list.reverse_()
my_list.show()