# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def print_age(self):
        print('name = %s, age = %s, score = %s' % (self.__name, self.__gender, self.score))

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


if __name__ == '__main__':
    s = Student("Edwin5", 25)
    s.score = 99
    s.print_age()
