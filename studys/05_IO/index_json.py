import json
from io import StringIO, BytesIO


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def sayHi(self):
        print('Hi~ I am %s' % self._name)


per1 = Person('Jack', 20)
per2 = Person('刘德华', 65)

print(per1.__dict__)

print(json.dumps(per1, default=lambda obj: obj.__dict__))

print(json.dumps(per2, default=lambda obj: obj.__dict__, ensure_ascii=False))

# json.dumps()和json.dump()本质上是一样的
with open('file/per1.json', 'w') as f1:
    # f1.write(json.dumps(per1, default=lambda obj: obj.__dict__))
    json.dump(per1, f1, default=lambda obj: obj.__dict__)

s1 = StringIO()
json.dump(per2, s1, default=lambda obj: obj.__dict__, ensure_ascii=False)

print(s1.getvalue())
