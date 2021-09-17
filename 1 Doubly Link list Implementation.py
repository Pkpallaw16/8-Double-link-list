class DoublyLinkedList:
    class Node:
        def __init__(self,data=0,prev=None,next=None):
            self.data=data
            self.prev=prev
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def handleAddWhenSizeZero(self,data):
        nn=self.Node(data)
        self.head=self.tail=nn
        self.size=1
    def addFirst(self,data):
        if self.size==0:
            self.handleAddWhenSizeZero(data)
        else:
            nn = self.Node(data)
            self.head.prev = nn
            nn.next=self.head
            self.head=nn
            self.size += 1
    def addLast(self,data):
        if self.size==0:
            self.handleAddWhenSizeZero(data)
        else:
            nn = self.Node(data)
            self.tail.next = nn
            nn.prev=self.tail
            self.tail=nn
            self.size += 1
    def getNodeAt(self,n):
        temp=self.head
        for i in range(n):
            temp=temp.next
        return temp
    def addAt(self,data,pos):
        if pos<0 or pos>self.size:
            print("-1")
            return
        elif pos==0:
            self.addFirst(data)
        elif pos==self.size:
            self.addLast(data)
        else:
            nn=self.Node(data)
            nm1=self.getNodeAt(pos-1)
            nn.next=nm1.next
            nm1.next.prev=nn
            nn.prev=nm1
            nm1.next=nn
            self.size+=1
    def addAfter(self,data,node):
        if node==self.tail:
            self.addLast(data)
            return
        else:
            nn=self.Node(data)
            nn.prev=node
            nn.next=node.next
            node.next.prev=nn
            node.next=nn
            self.size+=1
    def addBefore(self,data,node):
        if node==self.head:
            self.addFirst(data)
            return
        nn=self.Node(data)
        nn.prev=node.prev
        node.prev.next=nn
        nn.next=node
        node.prev=nn
        self.size+=1
    def displayForward(self):
        temp=self.head
        print("[",end="")
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print("]")

    def displayBackward(self):
        temp=self.tail
        print("[",end="")
        while temp!=None:
            print(temp.data,end=" ")
        print("]")
    def handleRemoveWhenSize1(self):
        val=self.head.data
        self.head=self.tail=None
        self.size=0
        return val
    def removeFirst(self):
        if self.size==0:
            print("ListIsEmpty")
            return -1
        elif self.size==1:
            self.handleRemoveWhenSize1()
        else:
            val=self.head.data
            self.head=self.head.next
            self.head.prev=None
            self.size-=1
            return val
    def removeLast(self):
        if self.size==0:
            print("ListIsEmpty")
            return -1
        elif self.size==1:
            self.handleRemoveWhenSize1()
        else:
            val=self.tail.data
            self.tail=self.tail.prev
            self.tail.next=None
            self.size-=1
            return val
    def removeAt(self,pos):
        if pos<0 or pos>self.size:
            print("ListIsEmpty")
            return -1
        elif pos==0:
            self.removeFirst()
        elif pos==self.size-1:
            self.removeLast()
        else:
            node=self.getNodeAt(pos)
            return self.removeNode(node)
    def removeAfter(self,node):
        if node.next==None:
            print("LocationIsInvalid: ")
            return -1
        return self.removeNode(node.next)
    def removeBefore(self,node):
        if node.prev==None:
            print("LocationIsInvalid: ")
            return -1
        return self.removeNode(node.prev)
    def removeNode(self,node):
        if node==self.head:
            return self.removeFirst()
        elif node==self.tail:
            return self.removeLast()
        val=node.data
        nm1=node.prev
        np1=node.next
        nm1.next=np1
        np1.prev=nm1
        self.size-=1
        return val
    def getFirst(self):
        if self.size==0:
            return -1
        return self.head.data
    def getLast(self):
        if self.size==0:
            return -1
        return self.tail.data
    def getAt(self,pos):
        if pos<0 or pos>=self.size:
            return -1
        return self.getNodeAt(pos).data
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False