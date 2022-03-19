
dic = {'a':['b','c','d']}
path = ['a']

a = dic['a']
a.remove('b')

print(dic)
# for index, forward in enumerate(dic.get(path[-1])):
#     copyDic = dic.copy()
#     copyDic[path[-1]] = copyDic[path[-1]][:index] + copyDic[path[-1]][index+1:]
#     print(copyDic[path[-1]])
    # print(copyDic[path[-1]][index+1:])

