immutable_var = 1,2,True,'af'
print(immutable_var)
immutable_var = 1,2,True,'af'
print(type(immutable_var))
#immutable_var[2] = 44 выдаст ошибку TypeError: 'tuple' object does not support item assignment
#print(immutable_var)
mutable_list = [1,2,False,"gdf"]
print(mutable_list)
print(type(mutable_list))
mutable_list[0] = 88
mutable_list[1] = True
mutable_list[2] = 'ASDF'
mutable_list[3] = 44
print(mutable_list)