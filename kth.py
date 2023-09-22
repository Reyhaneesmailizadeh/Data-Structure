
def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]

class MinHeap:

    def __init__(self):
        self.nodes = []
        self.currentsize = 0


    def bubble_up(self, index):

        stop = False
        while ((index - 1) // 2) >= 0 and stop == False:
            if self.nodes[index] < self.nodes[(index - 1) // 2]:
                self.nodes[index], self.nodes[(index - 1) // 2] = self.nodes[(index - 1) // 2], self.nodes[index]
            else:
                stop = True
            index = (index - 1) // 2


    def bubble_down(self, index):
        while (index * 2 + 1) <= self.currentsize - 1:
            mch = self.find_min_child(index)
            if self.nodes[index] > self.nodes[mch]:
                self.nodes[mch], self.nodes[index] = self.nodes[index], self.nodes[mch]
            index  = mch
    
    def heap_push(self, value):
        val = value
        self.nodes.append(int(val))
        self.currentsize += 1
        self.bubble_up(self.currentsize - 1)
        
    def heap_pop(self):

        if self.currentsize == 0:
            raise Exception ('empty or k > heap.currentsize')
        
        root = self.nodes[0]
        self.nodes[0] = self.nodes[self.currentsize - 1]
        self.nodes.pop()
        self.currentsize -= 1
        self.bubble_down(0)
        return root
        

    def find_min_child(self, index):


        if self.currentsize == 0 or index > self.currentsize - 1:
            raise Exception('out of range index')

        
        if (2 * index +2) > self.currentsize - 1:
            return index *2 + 1
        else:
            if self.nodes[index * 2 + 1] < self.nodes[index * 2 + 2]:
                return index * 2 + 1
            else:
                return index * 2 + 2
        

    def heapify(self, *args):
        for i in args:
            self.heap_push(i)

    def getmin(self):
        return self.nodes[0]

    def sortnodes(self):
        sortedheap = []
        sortedheap = self.nodes
        sortedheap.sort()
        return sortedheap

    def getheap(self):
        return self.nodes
    
    def removee(self, element):
        i = self.nodes.index(element)
        self.nodes[i] = self.nodes[self.currentsize - 1]
        self.nodes.pop()
        self.currentsize -= 1
        if self.nodes[i] < self.nodes[(i - 1) // 2]:
            self.bubble_up(i)
        else:
            self.bubble_down(i)

info = []
info = input().split(' ')
array = []
array = input().split(' ')

sortedarray = MinHeap()
array.pop()
for t in array:
    sortedarray.heap_push(t)


sortedlist = []
sortedlist= sortedarray.sortnodes()
k = int(info[2])
l = int(info[0])

for i in range(int(info[1])):
    tmp = []
    tmp = input().split(' ')
    if tmp[0] == 'print':
        if k > l:
            print('-1')
        else:
            tmp2 = []
            tmp2 = sortedlist[k - 1]
            print(tmp2)

    elif tmp[0] == '-':
        l -= 1
        kthsmallest = kthSmallest(sortedlist, k)
        sortedarray.removee(kthsmallest)
        sortedlist= sortedarray.sortnodes()

    else:
        sortedarray.heap_push(tmp[1])
        sortedlist= sortedarray.sortnodes()
        l += 1
