
#字典方式传参：
def unpack_dic(name,age):  #name=“alex” age=“16”
    print(name,age)

data_dic = {"name":"alex","age":16}

#unpack_dic(**data_dic)  #name="alex",age=16
print(type({**data_dic}))

# if __name__ == '__main__':
#     # 下面属于字典的解包操作我们可以使用两个**这样就可以将字典解包成key=value的形式
#     dic = {"name": "zhaozhao", "password": "123456"}
#     dic_fun(**dic)


# a, b, *c = [1, 2, 3, 4]
# print(a, b, c)
#
# a, *b, c = [1, 2, 3, 4]
# print(a, b, c)