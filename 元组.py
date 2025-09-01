t1 = (1,"hi",True)
t2 = ()
t3 = tuple()
print(type(t1),t1)
print(type(t2),t2)
print(type(t3),t3)
t4 = ("hello",)
print(type(t4),t4)
t5 = ("hello")
print(type(t5),t5)
t6 = ((1,2,3),(4,5,6))
print(type(t6),t6)
num = t6[1][2]
print(num)
# index查找
t1 = (1,"hi",True)
index = t1.index(1)
print(index)
# count
t1 = (1,1,1,1,"hi",True)# Ture也是1
num = t1.count(1)
print(num)
# len
t1 = (1,1,1,1,"hi",True)
num = len(t1)
print(num) 
# while遍历
t1 = (1,1,1,1,"hi",True)
index = 0
while index < len(t1):
    print(t1[index])
    index+=1
# for遍历
for element in t1:
    print(element)
    







