my_str = "abcdefj hijklmn opqrst uvwxyz abcdefj"
value1 = my_str[2]
value2 = my_str[-16]
print(value1,value2)
# index
value = my_str.index("bc")
print(value)
# replace
new_my_str = my_str.replace("ab","nh")
print(new_my_str)
# split 
my_str = "abcdefj hijklmn opqrst uvwxyz abcdefj"
my_str_list = my_str.split(" ")
print(my_str_list,type(my_str_list))
# strip
my_str = "   abcdefj hijklmn opqrst uvwxyz abcdefj "
new_my_str = my_str.strip()
print(new_my_str)
my_str = "12abcdefj hijklmn opqrst uvwxyz abcdefj21"
print(my_str.strip("12"))
# 统计某字符串出现次数
my_str = "abcdefj hijklmn opqrst uvwxyz abcdefj"
count = my_str.count("a")
print(count)
# 统计长度
num = len(my_str)
print(num)



