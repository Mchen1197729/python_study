import pickle

# 将可序列化对象序列化
d = dict(name='Tom', age=29, gender='Female')

# pickle.dumps()方法把任意对象序列化成一个bytes
print(pickle.dumps(d))

# pickle.dump(obj,file) 将可序列化的对象直接写入文件
with open('./data/d.txt', 'wb') as fd:
    pickle.dump(d, fd)

# pickle.load()方法反序列化一个文件中的内容
with open('./data/d.txt', 'rb') as fr:
    print(pickle.load(fr))
