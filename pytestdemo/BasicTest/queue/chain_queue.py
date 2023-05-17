#链式队列
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def enqueue(self,item):
        if self.tail is None:
            new_node = self.Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next
    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    class Node:
        def __init__(self,data) ->None:
            self.data = data
            self.next = None

def test_queue():
    a = Queue()
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    deque_item = a.dequeue()
    assert deque_item == "10"
    assert a.head.data == "20"
    assert a.head.next.data == "30"

if __name__=="__main__":
    test_queue()