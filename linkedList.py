class LinkedList: #The actual list. Nodes are added to it.
    def __init__(self):
        self.head = None #head is the index in nodes first item in the list, we don't know it yet so call it None (Null)
        self.last = None #last is the index in nodes of the last node
        self.nodes = [] #in other languages, nodes could be stored in memory and pointers would be to mem addresses. Here, I use this list as "memory" - indexes in this list are memory addresses.

    def __str__(self): #When list converted to string.
        output = "[" #We print it in form [data1,data2,data3,...,data9,]
        currNodePtr = self.head #the address of the first node is stored in the head attribute of the list.
        while currNodePtr != None: #next only is None when the current Node's pointer is None, meaning the current node is the last node.
            data = self.nodes[currNodePtr]._data #gets the data from the current node and appends it to the output string.
            output += f"{data},"
            currNodePtr = self.nodes[currNodePtr]._ptr #sets the current node pointer to the pointer of the next node (stored in the current node's ptr var)
        output += "]"
        return output
    
    def add_node_front(self, data): #add a node to the front of the linked list.
        newNode = Node(data, self.head) #declare new node, the address of the current first node is stored in the head var currenty. This is now stored in the ptr var of this new node as it comes after the new front node.
        self.nodes.append(newNode) #add new node into "memory". Added to the end as order in memory doesn't matter.
        self.head = len(self.nodes)-1 #the head variable of the list is set to the "address" of the new node, which is the last valid index of the list acting as "memory".
        if len(self.nodes) == 1: #If this is the first item added to the list, the last var also needs to be set to the address of the new node.
            self.last = self.head

    def add_node_back(self, data): #add a node to the back of the linked list.
        newNode = Node(data) #declare new node. End of linked list so ptr will be None which is the default.
        self.nodes.append(newNode) #add into "memory"
        try:
            self.nodes[self.last]._ptr = len(self.nodes)-1 #the last var points to the ex-last node in the list. That node's ptr now needs to be the "address" of the new node (last index in the list acting as "memory")
            self.last = len(self.nodes)-1 #the last var now needs to be updated to be the "address" of the new node (again last index in the list acting as "memory")
        except TypeError: #falls apart if this is first node, as there is not ex-last node to amend. Get TypeError as passing None (default value of last var) as an index.
            self.head = 0 #set head and last to "address" of new node (0 as only, therefore first, item in "memory").
            self.last = 0

    def get_item_by_index(self, index): #get item by its index in the linked list (0 is first node in linked list, not in "memory" (nodes list))
        currNodePtr = self.head #the pointer of the current Node, starting with the first node in the linked list.
        for i in range(index): #If index is n, the node is the (n+1)th node in the linked list. We have the first, so we need to find the next node n times.
            currNodePtr = self.nodes[currNodePtr]._ptr #Set the current node pointer to the "address in memory" of the next node (stored in current node's ptr var)
        data = str(self.nodes[currNodePtr]) #We now have the "address in memory" of the required node so we return its data as a string.
        return data

    def update_last(self): #a method to update the last var of the linked list
        currNodePtr = self.head #start with the first node's "address in memory" stored in the current-node-pointer variable.
        nextNodePtr = self.nodes[currNodePtr]._ptr #get the next node's "address in memory", stored in the current node's ptr var, and store it in the next-node-pointer var.
        while nextNodePtr != None: #if the next-node-pointer is None, the current node is the last in the list. Otherwise we set the current-node-pointer to the address stored in next-node-pointer and get the next-node-pointer as before
            currNodePtr = nextNodePtr
            nextNodePtr = self.nodes[currNodePtr]._ptr
        self.last = currNodePtr #keeps getting next node until the current node is the last in the list, so we store the current nodes "address in memory" in the list's last var.

    def delete_node_by_index(self, index): #delete item by its index in the linked list (0 is first node in linked list, not in "memory" (nodes list))
        delNodePtr = self.head #the "address in memory" of the node to delete is stored in delete-node-pointer. Set to the "address in memory" of the first node.
        currLinkedListIndex = 0 #starts by considering the first item in the linked list.
        while currLinkedListIndex < index: #if the item being considered is earlier in the linked list than the node to delete, this block runs.
            delNodePtr = self.nodes[delNodePtr]._ptr #consider the next item in the list by getting its "address in memory" from the current node, and incrementing the current index in the Linked list by 1.
            currLinkedListIndex += 1
        
        #once we escape the loop, we know that the node that was being considered was the one that needed deleting so delNodePtr now stores the "address in memory" of the node to be deleted.
        
        #Because I am using a list to represent memory, a weird thing happens when you delete a node. The "address in memory" of any item that is stored after the deleted node in "memory" decreases by one as the deleted node is
        #removed from the list. If we were using memory, this wouldn't be a problem, we'd just have to update the pointer of the node before the one being deleted so that it points to the one after the deleted node.
        currNodePtr = self.head
        if self.head == delNodePtr:
            self.head = self.nodes[delNodePtr]._ptr

        if self.head > delNodePtr:
            self.head -= 1
        for i in range(len(self.nodes)):
            nextNodePtr = self.nodes[currNodePtr]._ptr
            if nextNodePtr != None:
                if nextNodePtr > delNodePtr:
                    self.nodes[currNodePtr]._ptr -= 1
                elif nextNodePtr == delNodePtr:
                    self.nodes[currNodePtr]._ptr = self.nodes[delNodePtr]._ptr
                    if self.nodes[delNodePtr]._ptr != None:
                        if self.nodes[delNodePtr]._ptr > delNodePtr:
                            self.nodes[currNodePtr]._ptr -= 1
        
            currNodePtr = nextNodePtr
        del self.nodes[delNodePtr]
        
        self.update_last()

class Node:
    def __init__(self, data, ptr=None):
        self._data = data #stores the nodes data
        self._ptr = ptr #don't know if there is a Node after it so ptr set to Null (None) by default.
    
    def __str__(self):
        return str(self._data)

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

