# 给出两个非空的链表用来表示两个非负的整数。
# 其中，它们各自的位数是按照逆序的方式存储的，且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以0开头。
# 示例：
# 输入：(7 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：2 -> 1 -> 8
# 原因：347 + 465 = 812
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 创建一个空链表保存结果
        re = ListNode(0)
        r = re # 指向首指针
        # 保存十进位之后的结果
        carry=0
        while(l1 or l2):
            # 判断是否l1和l2都存在值
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s=x+y+carry
            carry = s//10
            # 让首指针的next值为s%10
            r.next = ListNode(s%10)
            # r指向下一个值
            r=r.next
            # 向下一个节点取值
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        # 循环结束收，注意如果有进位需要保存
        if(carry>0):
            r.next = ListNode(1)
        return re.next
        
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"
a = Solution()
print(a.addTwoNumbers([2,4,3],[5,6,4]))