class ArrayStack:
    def __init__(self,n)->None:
        self.data = (-1)*n
        self.n = n
        self.count = 0
    def push(self,value):
        if self.n == self.count:
            return False
        self.data[self.count] = value
        self.count +=1
        return True
    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.data(self.count)

def test_static():
    array_stack = ArrayStack(5)
    data = ["a","b","c","d","e"]
    for i in data:
        array_stack.push(i)
    result = array_stack.push("a")
    assert not result
    data.reverse()
    for i in data:
        assert i == array_stack.pop()
    assert array_stack.pop() is None

if __name__ == '__main__':
    test_static()