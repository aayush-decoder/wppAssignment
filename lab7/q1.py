class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data, pos=None):
        newnode = Node(data)
        if pos is None or pos == 0:
            newnode.next = self.head
            self.head =newnode
            return
        temp = self.head
        count =0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if temp:
            newnode.next= temp.next
            temp.next= newnode
        else:
            print("Position out of range, insert at end.")
            self.insert(data)
    
    def delete(self, pos):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            return
        prev = None
        count=0
        while temp and count < pos:
            prev = temp
            temp = temp.next
            count +=1
        if temp:
            prev.next = temp.next
        else:
            print("Position out of range.")
    
    def diplay(self):  
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert(3)
ll.insert(8) 
ll.insert(1, 1)
ll.diplay()  
ll.delete(1)
ll.diplay()