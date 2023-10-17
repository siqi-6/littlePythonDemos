"""
字段
"""

def main():
  scores={'张三':98,'李四':88,'王五':77}
  print(scores['张三'])
  print(scores['李四'])

  for elem in scores:
    print('%s-->%d'%(elem,scores[elem]))

  #往后面添加了元素
  scores.update(leng=100)
  print(scores)
  if '呜呜呜' in scores:
    print(scores['呜呜呜'])
  print(scores.get('呜呜呜'))
  print(scores.get('呜呜呜',60))

  #弹出倒数第一个
  print(scores.popitem())
  print(scores.popitem())

  #弹出value
  print(scores.pop('张三',98))

  #清空元素
  scores.clear()
  print(scores)

  #打印
  print(scores)
  print(scores.keys())
  print(scores.values())
  print(scores.items())

  for elem in scores.items():
    print(elem)
    print(elem[0],elem[1])
  if '张三' in scores:
    scores['张三']=900
  print(scores)
  scores.setdefault('五五五五',888)
  print(scores)
  #第二次用会失效
  scores.setdefault('五五五五',8)
  print(scores)
  scores['五五五五']=88
  print(scores)


if __name__=='__main__':
  main()