#coding=utf-8

place = ['B','A','C','E','D']
#原始顺序
print('原始顺序是：')
print(place)
#sorted临时排序
print('临时排序：')
print(sorted(place))
#原始顺序
print('原始顺序：')
print(place)
#reverse排序  永久  但可修改
print('reverse永久倒序排序')
place.reverse()
print(place)

#列表长度
print(len(place))