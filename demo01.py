# print(type("dsaddsa"))
# print(type(232))
# print(type(2.32))
# print(type(True))
# print(type([]))
# print(type(()))
# print(type({}))
# a = input('请输入内容1：')
# b = input('请输入内容2：')
# c = int(len(a))
# d = int(len(b))
# print('内容1为：'+a+'\n'+'内容2为：'+b+'\n'+'两组内容的长度为：',c+d)
# if c>d:
#     print('内容1比内容2长')
# else:
#     print('内容1比内容2短')
#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'X',j,'=',i*j,end=' ')
    print()