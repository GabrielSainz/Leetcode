'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        pass

list1 = [1,3,5,6]
list2 = [2,4,7]

list0 = []
h = 0
i = 0
while (h != len(list1)-1) or (i != len(list2)-1):
    print(i, h)
    if list1[h] < list2[i]: 
        list0.append(list1[h])
        h += 1
    else: 
        list0.append(list2[i])
        i += 1
    print(list0)

print(list0)
        