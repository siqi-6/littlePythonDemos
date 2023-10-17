"""
数组
"""

# % 后面是字符串用s 整数用d 两位数.1f
# 字符串直接用input
# if = 后面用字符串
# %后面有两项用括号
# %=组合打出 后面%（）用逗号隔开

def main():
  numbers = int(input('请输入学生数量: '))
  names = [None] * numbers
  scores = [None] * numbers
  for index in range(len(names)):
    names[index] = input('请输入第%d个学生名字: ' % (index + 1))
    scores[index] = float(input('请输入第%d个学生分数: ' % (index + 1)))
  total = 0
  for index in range(len(names)):
    print('%s:%.1f分'%(names[index],scores[index]))
    total+=scores[index]
  print('平均成绩是：%.1f分'%(total/numbers))

if __name__=='__main__':
  main()

