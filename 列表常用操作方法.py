# 1.查找某元素的下标索引
my_list = ["nh",666,True]
index = my_list.index("nh")
print(index)
# 2.修改特定下标索引的值
my_list[0] = "zj"
print(my_list[0])
# 3.在指定下标位置插入新元素
my_list.insert(1,"ywz")
print(my_list)
# 4.在尾部追加元素
my_list.append("best")
print(my_list)
# 5.在尾部追加一批元素
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(my_list)
# 6.删除
my_list = ["nh",666,True]
# 6.1del
del my_list[2]
print(my_list)
#6.2pop
my_list = ["nh",666,True]
element = my_list.pop(2)
print(my_list)
print(element)
# 7.删除某元素在列表中的第一个匹配项
my_list = ["nh",666,True,666]
my_list.remove(666)
print(my_list)
# 8.清空列表
my_list.clear()
print(my_list)
# 9.统计某元素的数量
my_list = ["nh",666,True,666]
count = my_list.count(666)
print(count)
# 10.统计列表中全部元素数量
my_list = ["nh",666,True,666]
count = len(my_list)
print(count)





