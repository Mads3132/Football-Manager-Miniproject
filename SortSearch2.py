#Set-up a singular node
#sdjasnjdinsa
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

#Create a single linked list
class SLinkedList:
    def __init__(self):
            self.headval = None

with open('players.txt') as f:
    content = f.read()
    words = content.splitlines()
    scontent = sorted(words)
print(scontent[0, 1, 2])
print(scontent[1])

list1 = SLinkedList()
list1.headval = Node(scontent[0])
i = 0
while i < len(scontent):
    i += 1
    e2 = Node(scontent[1])

#Link first node to second node
list1.headval.nextval = e2


#Member function to print list in console
def listprint(self):
    printval = self.headval
    while printval is not None:
        #print (printval.dataval)
        printval = printval.nextval

#Member to insert at beginning of node
def AtBegining(self, newdata):
    NewNode = Node(newdata)
#Update the new nodes next val to existing node
    NewNode.nextval = self.headval
    self.headval = NewNode

#Member to insert at the end of node
def AtEnd(self, newdata):
    NewNode = Node(newdata)
    if self.headval is None:
        self.headval = NewNode
        return
    laste = self.headval
    while(laste.nextval):
        laste = laste.nextval
    laste.nextval=NewNode

listprint(list1)
