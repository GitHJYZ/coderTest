#循环队列
class Queue():
    def __init__(self,capactity)->None:
        self.n = capactity
        self.items = [-1]*capactity
        self.head = 0
        self.tail = 0
    def enqueue(self,item):
        if self.tail + 1 % self.n == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        return True
    def dequeue(self):
        if self.tail == self.head:
            return None
        value = self.items[self.head]
        self.head = (self.head + 1)% self.n
        return value


def test_queue():
    a = Queue(3)
    a.enqueue("10")
    a.enqueue("20")
    result = a.enqueue("30")
    assert not result
    a.dequeue()
    a.enqueue("30")
    assert a.items[2] == "30"
    result = a.enqueue("10")
    assert not result

if __name__ == "__main__":
    test_queue()