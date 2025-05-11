class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data : %s>" % self.data



class LinkedList:
        """
        Singly Linked List
        """
        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head == None

        def size(self):

            """
            returns the number of items in the list
            Takes O(n) time
            """
            current = self.head
            count = 0

            while current:
                count +=1
                current = current.next_node

            return count



        def add(self, data):
            """
            Adds a new node containing data at head of the list
            Takes O(1) time
            """
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

        def search(self, key):
            """
            Returns the node or None if not found
            Takes O(n) or linear time
            """
            current = self.head

            while current:
                if current.data ==key:
                    return current
                else:
                    current = current.next_node

            return None


        def insert(self, data, index):
            """
            Insertion takes O(1) time but finding the node at the insertion point takes O(n) time.
            Takes an overall O(n) time.
            """
            if index == 0:
                self.add(data)
            
            if index>0:
                new = Node(data)
                
                position = index
                current = self.head

                while position > 1:
                    current = current.next_node
                    position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new
                new.next_node = next_node
                
        def remove(self, key):
            """
            Takes O(n) time.
            """

            current = self.head
            previous = None
            found = false

            while current and not found:
                if current.data == key and current is self.head:
                    found = True
                    self.head = current.next.node
                elif current.data == key:
                    found = True
                    previous.next_node = current.next_node
                else:
                    previous = current
                    current = current.next_node
            return current


        def node_at_index(self, index):
            if index ==0 :
                return self.head
            else: 
                current = self.head
                position = 0

                while position < index:
                    current = current.next_node
                    position += 1

                return current


        def reverseList(self):
            """
            Takes O(n) time and O(1) space
            """
            prev = None 
            current = self.head

            while current:
                next = current.next_node
                current.next_node = prev
                prev = current
                current = next
            self.head = prev
            return self
            

        def reverseList_recursive(self):
            prev = None
            current = self.head

            if current:
                return prev
            
            next = current.next_node
            current.next_node = prev
            return reverseList_recursive()

        def __repr__(self):
            """
            Returns a string representation of the list.
            Takes O(n) time
            """
            nodes = []
            current = self.head

            while current:
                if current is self.head:
                    nodes.append("[Head: %s]" %current.data)
                elif current.next_node is None:
                    nodes.append("[Tail: %s]" % current.data)
                else:
                    nodes.append("[%s]" %current.data)
                
                current = current.next_node
            return '->'.join(nodes)