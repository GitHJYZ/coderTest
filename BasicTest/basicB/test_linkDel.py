class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0,head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

def test_num():
    head = [1,2,3,3,4,4,5]
    s = Solution()
    res = s.deleteDuplicates(head)
    print(res)
