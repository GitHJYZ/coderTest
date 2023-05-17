class BinarySerchTree:
    def __init__(self) -> None:
        self.tree = None
    class Node:
        def __init__(self,data) -> None:
            self.data = data
            self.left = None
            self.right = None

    def insert(self,value):
        #如果是根节点，直接插入
        if self.tree == None:
            self.tree = self.Node(value)
            return
        p = self.tree
        while p is not None:
            if value > p.data:
                if p.right is None:
                    p.right = self.Node(value)
                    return
                p = p.right
            elif value < p.data:
                if p.left is None:
                    p.left = self.Node(value)
                    return
                p = p.left

    def find(self,value):
        p = self.tree
        while p is not None:
            if value > p.data:
                p = p.right
            elif value < p.data:
                p = p.left
            else:
                return p
        return None
    def delete(self,value):
        p = self.tree
        pp = None
        while p is not None and p.data != value:
            pp = p
            if value > p.data:
                p = p.right
            elif value < p.data:
                p = p.left

            if p is None:
                return
            if p.left is not None and p.right is not None:
                tmp_p = p.right
                tmp_pp = p
                #找要删除结点的右子树中最小值
                while tmp_p.left is not None:
                    tmp_pp = tmp_p
                    tmp_p = p.left
                p.data = tmp_p.data
                p = tmp_p
                pp = tmp_pp

            if p.left is not None:
                child = p.left
            elif p.right is not None:
                child = p.right
            else:
                child = None
            # 删除根结点
            if pp is None:
                self.tree = child
            elif pp.left is p:
                pp.left = child
            elif pp.right is p:
                pp.right = child
    def pre_order(self,node):
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)
    def in_order(self,node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)
    def post_order(self,node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
def test_binary_search_tree():
    binary_search_tree = BinarySerchTree()
    data = [1,10,20,40,13]
    for i in data:
        binary_search_tree.insert(i)
    assert 20 == binary_search_tree.find(20).data
    binary_search_tree.delete(20)
    assert binary_search_tree.find(20) is None
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.tree)
    print("-----------------------")
    #1 10 13 40
    binary_search_tree.in_order(binary_search_tree.tree)
    print("-----------------------")
    binary_search_tree.post_order(binary_search_tree.tree)

if __name__ == '__main__':
    test_binary_search_tree()
