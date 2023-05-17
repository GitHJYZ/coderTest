#普通队列
class Queue:
    def __init__(self,capacity)->None:
        self.n = capacity
        self.items = [-1]*capacity
        self.head = 0
        self.tail =0
    def enqueue(self,item):
        if self.tail == self.n:
            return False
        self.items[self.tail] = item
        self.tail +=1
    def dequeue(self):
        if self.head == self.tail:
            return False
        value = self.items[self.head]
        self.head += 1
        return value

def test_queue():
    a = Queue(10)
    a.enqueue("10")
    a.enqueue("20")
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[a.head] == "20"
    assert a.items[a.tail-1] == "30"

if __name__=="__main__":
    test_queue()

# def test_num():
#     i = 2
#     while(i <= 100):
#         j = 2
#         while(j <=(i/j)):
#             if not (i%j):break
#             j +=1
#         if (j > i / j):
#             print(i,"是素数")
#         i +=1
#
# if __name__ =="__main__":
#     test_num()

def test_num():
    i = 2
    while(i <= 100):
        j = 2
        while(j <= (i/j)):
            if not i%j:break
            j +=1
        if j > (i/j):
            print(i,"素数")
        i +=1

if __name__=="__main__":
    test_num()