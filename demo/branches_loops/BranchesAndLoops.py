
# 分支

x =float(input('x='))
if x>1:
  y=3*x-1
elif x>=-1:
  y=x+2
else:
  y=5*x+3
print('f(%.2f)=%.2f'%(x,y))


username=input('请输入用户名: ')
password=input('请输入口令: ')
if username =='admin' and password=='123456':
  print('身份验证成功')
else:
  print('身份验证失败')


# 循环
# 1:前闭后开 2:从0开始 3:
# for 循环
sum=0
for x in range(1,10):
    sum+=x
print(sum)

sum=0
for x in range(1,4,2):
  sum+=x
print(sum)

#while 循环
sum, num=0,2
while num<=5:
  sum+=num
  num+=1
print(sum)
