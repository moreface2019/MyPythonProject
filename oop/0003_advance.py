print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>__slots__ 字段限制 & @property 属性>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Student(object):
    __slots__ = ('_score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 2015


s = Student()
s.score = 60
print('s.score =', s.score)
# >>>s.score = 60
print('s.age =', s.age)
# >>>s.age = 2015
