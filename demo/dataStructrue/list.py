"""
列表
"""
def fib(n):
  a,b=0,1
  for _ in range(n):
    a,b=b,a+b
    yield a

def main():
  fruits = ['apple', 'grape', 'waxberry']
  print(fruits)
  print(fruits[0])
  print(fruits[1])

  #遍历
  # 从右往左数 -1 开始
  print(fruits[-1])
  print(fruits[-3])


  # 更新
  fruits[0] = '@pple'
  print(fruits)


  #继续添加
  fruits.append('strawberry')
  print(fruits)
  #指定位置添加
  fruits.insert(0,'siqi')
  print(fruits)


  # 删除
  del fruits[1]
  print(fruits)
  fruits.pop()
  print(fruits)
  fruits.pop(1)
  print(fruits)
  fruits.remove('siqi')
  print(fruits)

  fruits+=['mango','pear']
  print(fruits)
  for fruit in fruits:
    print(fruit.title(),end=' ')
  print()
  #前开后币：切片
  fruits2 =fruits[1:3]
  print(fruits2)
  #创建新的引用,遍历
  fruits3=fruits[:]
  print(fruits3)
  #倒序打印
  fruits4=fruits[::-1]
  print(fruits4)
  #同一个元素有两个index，顺着数和倒着数，实际上还是从左往右打印
  # range 适合数组，其他的都是直接in 集合
  fruits5=fruits[-3:-1]
  print(fruits5)


  #创建数值列表
  list1= list(range(1,11))
  print(list1)

  list2 =[x*x for x in range(1,11)]
  print(list2)

  list3=[m+n for m in 'ANCDEFG' for n in '12345']
  print(list3)
  for elm in list3:
    print(elm,end='')
  print()
  gen=fib(2)
  print(gen)
  for elm in gen:
    print(elm,end='')
  print()


if __name__ == '__main__':
  main()
