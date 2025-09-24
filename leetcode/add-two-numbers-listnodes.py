#https://leetcode.com/problems/add-two-numbers/  if inputs were linked lists
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = ListNode(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.val, end=" -> ")
#             current = current.next
#         print("None")
# class Solution:
#     def addTwoNumbers(self, l1: [LinkedList], l2: [LinkedList]) -> [LinkedList]:
#         current1 = ListNode()
#         current2 = ListNode()
#         agg = 0
#         over = 0
#         sol = LinkedList()
#         current1 = l1.head
#         current2 = l2.head
#         while current1 :
#             print(current2.next)
#             agg=current1.val + current2.val + over
#             print(agg)
#             print(current2.val )
#             if (agg >= 10):
#                 over = agg //10
#                 agg=agg-10
#             else:
#                 over = 0
#             sol.append(agg)
#             sol.print_list()
#             current1 = current1.next
#             current2 = current2.next
#             if((current1 is None)and over !=0):
#                 sol.append(over)
#         sol.print_list()


# l1 = LinkedList()
# l1.append(2)
# l1.append(4)
# l1.append(3)
# l2 = LinkedList()
# l2.append(5)
# l2.append(6)
# l2.append(4)
# sol = Solution()
# sol.addTwoNumbers(l1,l2)
#https://leetcode.com/problems/add-two-numbers/submissions/1779625511/ if inputs were list nodes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        agg = 0
        over = 0
        sol = LinkedList()
        while l1 :
            if (l1.next is None and l2.next is not None):
                l1.next = 0
            if (l2.next is None and l1.next is not None):
                l2.next = 0

            agg=l1.val + l2.val + over

            if (agg >= 10):
                over = agg //10
                agg=agg-10
            else:
                over = 0
            sol.append(agg)
            sol.print_list()
            l1 = l1.next
            l2 = l2.next
            if((l1 is None)and over !=0):
                sol.append(over)
        sol.print_list()

