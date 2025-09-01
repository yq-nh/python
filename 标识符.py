# # 规则1:内容限定，只能用：中文，英文，数字，下划线；不能以数字开头
# # 错误代码示范： 1_name
# # 错误代码示范： name_!
# name_ = "zhangsan"
# _name = "zhangsan"
# name_1 = "zhangsan"
# # 规则2:大小写敏感
# Yq = "袁泉"
# yq = "你好"
# # 规则三不可使用关键字
# # 错误代码示范： class = 1
# # 关键字也大小写敏感
# Class = 1