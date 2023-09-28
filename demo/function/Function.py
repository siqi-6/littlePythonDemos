"""
基础操作
"""
#  整除
def factorial(n):
  result = 1
  for num in range(1, n + 1):
    result *= num
  return result


print(factorial(7) // factorial(3))


#  求最大公约数和最小公倍数
def gcd(x, y):
  if x > y:
    # 互换
    (x, y) = (y, x)
    # -1 就是倒叙 正数就是每隔n
    # 倒序包含了第2个值，非倒叙前闭后开
  for factor in range(x, 1, -1):
    if x % factor == 0 and y % factor == 0:
      return factor
  return 1


def lcm(x, y):
  return x * y // gcd(x, y)


print(gcd(15, 5))
print(lcm(15, 5))
import shutil
import time


def myfilter(str):
  return len(str) == 6


print(chr(0x9a86))
print(hex(ord('骆')))
#
# #绝对值
print(abs(-1.2345))

# #取整
print(round(-1.2345))

print(pow(1.2345, 5))

fruits = ['orange', 'peach', 'durian', 'watermelon']
# #前闭后开
print(fruits[slice(1, 3)])

# filter 以前面的标准过滤后面的集合
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)


"""
时间
"""
# 时间戳
seconds = time.time()
print(seconds)

# #获取当地时间
localtime = time.localtime(seconds)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)

# 欧洲时间
actime = time.asctime(localtime)
print(actime)

# 指定字符串
strTime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strTime)

# 转成日期
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

# 复制文件
# shutil.copy('/Users/Hao/hello.py')


"""
参数
"""

# 参数默认值 不传参就用默认值 没有默认值必须传参
def f1(a, b=5, c=10):
  return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
# 指定参数就按照指定值而不是位置的值
print(f1(c=2, b=3, a=1))


# 可变参数
def f2(*args):
  sum = 0
  for num in args:
    sum += num
  return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kw):
  if 'name' in kw:
    print('欢迎您%s!' % kw['name'])
  elif 'tel' in kw:
    print('您的联系电话%s!' % kw['tel'])
  else:
    print('没找到您的个人信息')


param = {'name': 'siqiliu', 'age': 26}
f3(**param)
f3(name='siqiliu', age=38, tel='13866778899')
f3(user='siqiliu', age=38, tel='13866778899')
f3(user='siqiliu', age=38, mobile='13866778899')



"""
作用域
"""

# 局部
def foo1():
  a = 5
foo1()

# 全局
b = 10
def foo2():
  print(b)
foo2()


def foo3():
  b = 100
  print(b)
foo3()  # 100
print(b)  # 10 只会读到全局


def foo4():
  global b  # 在方法内部定义全局变量
  b = 200
  print(b)
foo4()
print(b)
