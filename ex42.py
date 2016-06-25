# -*- coding: utff-8 -*-

## Animal은 object의 일종이다 (is-a) (네, 조금 헷갈리죠) 추가 점수 부분을 살퍼보세요
class Animal(object):
    pass

## Dog는 Animal의 일종이다 (is-a)
class Dog(Animal):

    def __init__(self, name):
        ## 이 인스턴스의 name 변수를 name으로 초기화 시킨다 (has-a)
        self.name = name

## Cat는 Animal의 일종이다 (is-a)
class Cat(Animal):

    def __init__(self, name):
        ## 이 인스턴스의 name 변수를 name으로 초기화 시킨다 (has-a)
        self.name = name

## Person은 object의 일종이다 (is-a)
class Person(object):

    def __init__(self, name):
        ## 이 인스턴스의 name 변수를 name으로 초기화 시킨다 (has-a)
        self.name = name

        ## Person은 어떤 종류의 pet을 갖고 있다 (has-a)
        self.pet = None

## Employee는 Person의 일종이다 (is-a)
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? 음 이 마법은 뭐죠?
        super(Employee, self).__init__(name)
        ## 이 인스턴스의 salary 변수를 salary으로 초기화 시킨다 (has-a)
        self.salary = salary

## Fish는 object의 일종이다 (is-a)
class Fish(object):
    pass

## Salmon은 Fish의 일종이다 (is-a)
class Salmon(Fish):
    pass

## Halibut는 Fish의 일종이다 (is-a)
class Halibut(Fish):
    pass


## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## satan은 Cat의 일종이다 (is-a)
satan = Cat("Satan")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")

## rover는 Dog의 일종이다 (is-a)
rover = Dog("Rover")
