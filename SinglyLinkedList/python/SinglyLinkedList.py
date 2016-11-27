class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printList(self):
        current = self.head
        full_list = ""
        while current != None:
            full_list += str(current.getData()) + " - "
            current = current.getNext()
        return full_list


if __name__ == "__main__":
    mylist = SinglyLinkedList ()
    mylist.add(31)
    mylist.add(32)
    mylist.add(36)
    mylist.add(37)
    mylist.add(38)
    mylist.add(31)
    print mylist.size()
    print mylist.search(35)
    print mylist.remove(31)
    print mylist.size()
    print mylist.printList()
