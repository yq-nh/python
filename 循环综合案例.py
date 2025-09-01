"""
发工资
发1w给20名员工
1.每人领1000元
2.绩效1-10，低于5不发
31w发完结束发工资
"""
money = 10000
for i in range(1,21):
    import random
    score = random.randint(1,10)
    if score < 5:
        print(f"员工{i}绩效分{score},不满足")
        continue

    if money >= 1000:
        money -= 1000
        print(f"{i}复合条件发1000，公司余额{money}")
    else:
        print(f"余额不足，下个月发")
        break