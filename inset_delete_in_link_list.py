class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None


    # TO ADD NODE(insert data into the list)

    def insertLast(self,data):
        newNode=node(data)
        if self.start==None:
            self.start=newNode

        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    # To VIEW THE LIST

    def viewList(self):
        if self.start==None:
            print('list is th empty')
        else:
            print('list elements are: ',end=' ')
            temp=self.start
            while temp!=None:
                print(temp.data,end='  ')
                temp=temp.next

    #  To DElete first
    def deleteFirst(self):
        if self.start==None:
            print('list is empty')
        else:
            print('deleted element is: ',self.start.data)
            self.start=self.start.next
            




    

mylist=LinkedList()
for i in range(int(input())):
    mylist.insertLast(int(input('enter element to list: ')))

mylist.viewList()
print()
mylist.deleteFirst()

mylist.deleteFirst()

mylist.deleteFirst()

mylist.deleteFirst()

mylist.deleteFirst()

mylist.deleteFirst()

mylist.deleteFirst()
