"""
对象
"""

class Student(object):

  def __init__(self,name,age):
    self.name=name
    self.age=age

# init 方法中没有定义的变量就不能用self.
  def study(self,course_name):
     print('%s正在学习%s.'%(self.name,course_name))

  def watchMv(self):
     if self.age<18:
        print('%s看《熊出没》'%self.name)
     else:
        print('%s看《白夜追凶》'%self.name)

  def __del__(self):
     print('销毁这个学生学习记录')


def main():
   a1 =Student('规权',80)
   a1.study('Python程序设计')
   a1.watchMv()

if __name__=='__main__':
  main()
