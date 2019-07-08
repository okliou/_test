import sys


class Employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


findword = 0

namedata = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

data = [[1001, 22222], [1002, 23451], [1003, 32456], [1004, 45678], [1005, 43214], [1006, 23332], [1007, 25552], ]

head = Employee()
if not head:
    # raise ValueError('内存分配失败！')
    print('内存分配失败！')
    sys.exit()

head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None
ptr = head
for i in range(1, 7):
    newnode = Employee()
    newnode.num = data[i][0]
    newnode.name = namedata[i]
    newnode.salary = data[i][1]
    newnode.next = None
    ptr.next = newnode
    ptr = ptr.next

ptr = head
i = 0
print('反转前节点数据：')
while ptr != None:
    print('[{}{}{}] =>'.format(ptr.num, ptr.name, ptr.salary), end='')
    i += 1
    if i >= 3:
        print()
        i = 0
    ptr = ptr.next

ptr = head
before = None
print('\n反转后节点数据：')
while ptr != None:
    last = before
    before = ptr
    ptr = ptr.next
    before.next = last

ptr = before
while ptr != None:
    print('[{}{}{}] =>'.format(ptr.num, ptr.name, ptr.salary), end='')
    i += 1
    if i >= 3:
        print()
        i = 0
    ptr = ptr.next
