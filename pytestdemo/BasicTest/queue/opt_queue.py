#优化队列
class Queue:
    def __init__(self,capacity)->None:
        self.n = capacity
        self.items = [-1]*capacity
        self.head = 0
        self.tail =0
    def enqueue(self,item):
        if self.tail == self.n:
            if self.head == 0:
                return False
            for i in range(self.head,self.tail):#数据迁移
                self.items[i - self.head] = self.items[i]
            self.tail -= self.head
            self.head = 0
        self.items[self.tail] = item
        self.tail +=1
    def dequeue(self):
        if self.head == self.tail:
            return False
        value = self.items[self.head]
        self.head += 1
        return value

def test_queue():
    a = Queue(3)
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    result = a.enqueue("40")
    assert not result
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[0] == "20"
    assert a.items[2] == "30"

if __name__=="__main__":
    test_queue()