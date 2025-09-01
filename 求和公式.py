i = 0 
j = 0
print("请输入想要求和的范围")
i = int(input())
j = int(input())
temp = i
sum = 0
while temp <= j:
    sum += temp
    temp += 1
print(sum)