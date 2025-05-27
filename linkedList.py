class LinkedList:
    def __init__(self):
        self.head = None #head is the index in nodes first item in the list, we don't know it yet so call it None (Null)
        self.last = None #last is the index in nodes
        self.nodes = []

    def __str__(self):
        output = "["
        next = self.head
        while next != None:
            data = self.nodes[next]._data
            output += f"{data},"
            next = self.nodes[next]._next
        output += "]"
        return output
    
    def add_node_front(self, data):
        newNode = Node(data, self.head)
        self.nodes.append(newNode)
        self.head = len(self.nodes)-1
        if len(self.nodes) == 1:
            self.last = self.head

    def add_node_back(self, data):
        newNode = Node(data)
        self.nodes.append(newNode)
        try:
            self.nodes[self.last]._next = len(self.nodes)-1
            self.last = len(self.nodes)-1
        except TypeError:
            self.head = 0
            self.last = 0

    def get_item_by_index(self, index):
        current = self.head
        for i in range(index):
            current = self.nodes[current]._next
        data = str(self.nodes[current])
        return data

    def update_last(self):
        currentIndexInNodes = self.head
        for i in range(len(self.nodes)):
            nextIndex = self.nodes[currentIndexInNodes]._next
            if nextIndex == None:
                self.last = currentIndexInNodes
            else:
                currentIndexInNodes = nextIndex

    def delete_node_by_index(self, index):
        nodeIndexToDelete = self.head
        currentPlaceInLinkedList = 0
        while currentPlaceInLinkedList < index:
            nodeIndexToDelete = self.nodes[nodeIndexToDelete]._next #ends up with index in nodes of item to del
            currentPlaceInLinkedList += 1
        
        del currentPlaceInLinkedList

        currentIndexInNodes = self.head
        if self.head == nodeIndexToDelete:
            self.head = self.nodes[nodeIndexToDelete]._next

        if self.head > nodeIndexToDelete:
            self.head -= 1
        for i in range(len(self.nodes)):
            nextIndex = self.nodes[currentIndexInNodes]._next
            if nextIndex != None:
                if nextIndex > nodeIndexToDelete:
                    self.nodes[currentIndexInNodes]._next -= 1
                elif nextIndex == nodeIndexToDelete:
                    self.nodes[currentIndexInNodes]._next = self.nodes[nodeIndexToDelete]._next
                    if self.nodes[nodeIndexToDelete]._next != None:
                        if self.nodes[nodeIndexToDelete]._next > nodeIndexToDelete:
                            self.nodes[currentIndexInNodes]._next -= 1
        
            currentIndexInNodes = nextIndex
        del self.nodes[nodeIndexToDelete]
        
        self.update_last()

class Node:
    def __init__(self, data, next=None):
        self._data = data #don't need next_pointer as may not know it when creating Node. Dealt with in LinkedList?
        self._next = next #don't know if there is a next so set to null (None)
    
    def __str__(self) -> str:
        return str(self.data)

stupid = LinkedList()

stupid.add_node_back("first")
print(str(stupid))
stupid.add_node_front("second")
print(str(stupid))
stupid.add_node_front("third")
print(str(stupid))
stupid.add_node_back("fourth")
print(str(stupid))

stupid.delete_node_by_index(0)
print(str(stupid))

