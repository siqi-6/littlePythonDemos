"""
set
"""


def main():
  # set1 = {1, 2, 3}
  # print(set1)
  # print('Length: ', len(set1))
  #
  # # 直接插入表
  # set2 = set(range(1, 11))
  # print(set2)
  #
  # # 添加元素
  # set1.add(22)
  # set2.update([33, 44])
  # print(set1)
  # print(set2)
  #
  # # 删除
  # set2.discard(5)
  # print(set2)
  # if 4 in set2:
  #   set2.remove(4)
  # print(set2)
  #
  # #遍历
  # for elem in set2:
  #   # *成 **平方
  #   # end 指定元素之间的间隔，没有就是分行，有看有无空格
  #   print(elem**2,end=' ')
  # print()
  #
  #
  # #集合转set
  # set3 =set((1,2,3,2,3,4,5))
  # #删除第一个元素
  # print(set3.pop())
  # print(set3)
  #


  #前闭后开
  set1=set(range(1,7))
  print(set1)
  #++2 指定间隔
  set2=set(range(2,11,2))
  print(set2)
  set3 =set(range(1,5))
  print(set3)

  #并
  print(set1&set2)
  #交
  print(set1|set2)
  #1对于2 的差集
  print(set1-set2)
  #去除了相同的部分
  print(set1^set2)
  print(set2<=set1)
  print(set3<=set1)
  print(set1 >= set2)
  print(set1 >= set3)

if __name__ == '__main__':
  main()
