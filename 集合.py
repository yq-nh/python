my_set = {"nh","nh","zj","zj",666,666}
my_set_empty = set()
print(my_set)
print(my_set_empty)
# add
my_set.add("excel")
my_set.add("666")
my_set.add("nh")
print(my_set)
# remove
my_set.remove("666")
print(my_set)
# 随机取出一个元素
my_set = {"nh","zj",666}
element = my_set.pop()
print(element)
print(my_set)
# clear
my_set.clear()
print(my_set)
#  取两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
print(set1.difference(set2))
# 消除差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(set1)
print(set2)
# union
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)
# len
set1 = {1,2,3,1,2,3,1,2,3}
print(len(set1))  
# 遍历
set1 = {1,2,3,4,5}
for element in set1:
    print(element)
