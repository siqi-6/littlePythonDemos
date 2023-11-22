"""
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: SiqiLiu
Date: 2023-09-28
"""

from random import randint

money=1000
while money>0:
  print('你的资产: ',money)
  need_go_on=False
  while True:
    debt=int(input('请下注'))
    if 0 < debt <=money:
      break
  first =randint(1,6)+randint(1,6)
  print('玩家摇出了%d点'%first)
  if first ==7 or first==11:
    money+=debt
    print('玩家胜')
  elif first ==2 or first==3 or first==12:
    money-= debt
    print('专家胜')
  else:
    need_go_on=True

  while need_go_on:
    next =randint(1,6)+randint(1,6)
    if next==7:
      money-= debt
      print('专家胜')
      need_go_on=False
    elif next==first:
      money+=debt
      print('玩家胜')
      need_go_on=False
print('你破产了')


