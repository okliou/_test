class student:
    def __init__(self):
        self.name = ''
        self.Math = 0
        self.Eng = 0
        self.no = ''
        self.next = None


head = student()
ptr = head
Msum = Esum = num = student_no = 0
select = 0

while select != 2:
    print('(1)新增 (2)离开 ==>')
    try:
        select = int(input('请输入一个选项：'))
        if select not in (1, 2):
            raise ValueError('输入错误')
    except ValueError:
        print('输入错误！')
        print('请重新输入\n')
    if select == 1:
        new_data = student()
        new_data.name = input('姓名：')
        new_data.no = input('学号：')
        new_data.Math = eval(input('数学成绩：'))
        new_data.Eng = eval(input('英语成绩：'))
        ptr.next = new_data
        new_data.next = None
        ptr = ptr.next
        num += 1

ptr = head.next
print()

while ptr != None:
    print('姓名:{}\t学号:{}\t数学成绩:{}\t英语成绩:{}'.format(ptr.name, ptr.no, ptr.Math, ptr.Eng))
    Msum += ptr.Math
    Esum += ptr.Eng
    student_no += 1
    ptr = ptr.next

if student_no != 0:
    print('-'*50)
    print('学生数学平均成绩：{}，英语平均成绩：{}'.format(Msum/student_no, Esum/student_no))
