import json
import pickle

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>序列化 pickling & 反序列化 unpickling>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print('# 序列化')
d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)
# >>>b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

print('# 反序列化')
reborn = pickle.loads(data)
print(reborn)
# >>>{'name': 'Bob', 'age': 20, 'score': 88}

print()

print('# JSON 序列化')
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
# >>>JSON Data is a str: {"name": "Bob", "age": 20, "score": 88}
reborn = json.loads(data)
print(reborn)


# >>>{'name': 'Bob', 'age': 20, 'score': 88}


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
# >>>Dump Student: {"name": "Bob", "age": 20, "score": 88}
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
# >>>Student object (Bob, 20, 88)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
# >>>{"name": "\u5c0f\u660e", "age": 20}
