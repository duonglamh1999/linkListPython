from logging import exception


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def get(self,ind):
        current = self.head
        counter = 0
        while current!=None and counter!= ind:
            current= current.next
            counter+=1
        return current
        
    def display (self):
        arr=[]
        cur=self.head
        while cur!=None:
            arr.append(cur.val)
            cur=cur.next
        print (arr)
    def push(self,data):
        newNode = Node(data)
        if self.head != None:
            current = self.head
            while current.next!=None:
                current= current.next
            current.next=newNode
        else:
            self.head = newNode
    def unshift(self,data):
        newNode = Node(data)
        if self.head != None:
            newNode.next = self.head
            self.head= newNode
        else: 
            self.head=newNode
    def pop(self):
        if self.head ==None:
            raise Exception("list empty")
        else:
            current = self.head
            while current.next!=None:
                if current.next.next==None:
                    current.next = None
                else:
                    current=current.next
    def shift(self):
        if self.head ==None:
            raise Exception("list empty")
        else:
            current = self.head
            self.head=current.next
    def getAt(self,index):
        if isinstance(index,int)==False:
            raise Exception("Wrong input type")
        else:
            return self.get(index).val
    def setAt(self,index,data):
        if isinstance(index,int)==False:
            raise Exception("Wrong input type")
        else:
            current =self.get(index)
            current.val = data
    def insertAt(self,index,data):
        if isinstance(index,int)==False:
            raise Exception("Wrong input type")
        else:
            newNode=Node(data)
            current =self.get(index-1)
            newNode.next = current.next
            current.next = newNode
    def removeAt(self,index):
        if isinstance(index,int)==False:
            raise Exception("Wrong input type")
        else:
            if index==0:
                self.shift()
            else:
                prev = self.get(index-1)
                prev.next= prev.next.next
    def average(self):
        cur = self.head
        total=0
        counter=0
        while cur!=None:
            total+= cur.val
            counter +=1
            cur= cur.next
        return total/counter





list1= LinkedList()
list1.push(1)
list1.push(3)
list1.push(4)
list1.insertAt(2,8)
print(list1.average())
list1.display()