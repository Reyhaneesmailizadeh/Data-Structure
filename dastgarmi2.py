import sys

class Stack():
    def __init__(self, size = 10):
        
        self.selfsize = size
        self.elements = []

    def isEmpty(self):
        if len(self.elements)==0:
            return True
        else:
            return False


    def push(self, value):
        self.elements.append(value)


    def pop(self):
        s = self.elements.pop()
        return s


    def put(self, value_):
        del self.elements[-1]
        self.elements.append(value_)


    def peek(self):
        return self.elements[-1]


    def expand(self):
        self.selfsize *= 2

        
    def getInOneLine(self):
        str = ""
        for i in range(len(self.elements)):
            str += self.elements[i] + " "
        return str


    def getSize(self):
        gs = len(self.elements)
        return gs


    def getCapacity(self):
        return self.selfsize


class Queue():
    def __init__(self):
        self.elements = []


    def getSize(self):
        gs = len(self.elements)
        return gs



    def enqueue(self, value):
        self.elements.insert(0, value)


    def dequeue(self):
        q = self.elements.pop()
        return q


    def isEmpty(self):
        if len(self.elements)==0:
            return True
        else:
            return False


    def getInOneLine(self):
        str = ""
        for i in range(len(self.elements)-1,-1,-1):
            str += self.elements[i] + " "
        return str


class Node():
     def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():


    def __init__(self):
        self.head = None
        


    def getList(self):
            Node = self.head
            ll = ""
            while (Node.next is not None):
                value = Node.val
                ll += value + " "
                Node = Node.next

            if Node.next is None:
                ll += Node.val

            return ll


    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = new_node

    def reverse(self):
        last = None
        current = self.head

        while current:
            next = current.next
            current.next = last
            last = current
            current = next
        self.head = last


classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()