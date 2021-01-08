# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>类 Class & 实例 Object>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Student(object):
    __slots__ = ('__name', '__score')
    gender = "M"

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.get_name())
# >>>bart.name = Bart Simpson
print('bart.score =', bart.get_score())
# >>>bart.score = 59
bart.set_score(46)
bart.print_score()
# >>>Bart Simpson: 46

print('grade of Bart:', bart.get_grade())
# >>>grade of Bart: C
print('grade of Lisa:', lisa.get_grade())
# >>>grade of Lisa: B

print(bart.gender)
# >>>M
print(Student.gender)
# >>>M
Student.gender = "B"
print(Student.gender)
# >>>B
