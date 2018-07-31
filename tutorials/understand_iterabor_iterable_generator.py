#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:10:41 2018

@author: allen
"""
# 1 what is an Iterator
class Iterator_A(object):
    def __next__(self):
        return "boom"

class Iterator_with_times_control(object):
    def __init__(self):
        self.i = 0
        
    def __next__(self):
        if self.i == 3:
            raise StopIteration()
        self.i += 1
        return "boom"

def test_iterator():
    iterator_a = Iterator_A()
    for i in range(4):
        print(iterator_a.__next__())
    
    iterator_b = Iterator_with_times_control()
    for i in range(4):
        print(iterator_b.__next__())
    
# 2 what is an Iterable
class Iterable_A(object):
    def __iter__(self):
        #overide __iter__ and return an Iterator
        return Iterator_with_times_control()

def test_iterable():
    a_iterable = Iterable_A() 
    for item in a_iterable:
        print(item)

# 3 combination of iterable with iterator 
class It(object): 
    #combined iterator with iterable
    def __init__(self):
        self.count = -1
    
    def __iter__(self):
        # return a iterator that must overide the __next__ method
        return self
    
    def __next__(self):
        self.count += 1
        if self.count < 4:
            return self.count * 2
        else:
            # A StopIteration exception is raised
            # to signal that the iterator is done
            # This is caught implicitly by the "for" loop
            raise StopIteration
            
def some_func():
    return It()

def test_iterator_iterable():
    iterable_iterator = some_func()
    for item in iterable_iterator:
        print(item)

def test_iterator_iterable_2():
    #for more insight as to whats happening behind the scenes, the for loop can be rewritten to this
    iterable_iterator = some_func()
    try:
        while 1:
            print(iterable_iterator.__next__())
    except StopIteration:
        pass
#does this make more sense or just confuse you more?
        
# 4 what is generator?
#genarator is an iterable_iterator object achieved by yield
def some_function():
    for i in range(4):
        yield i * 2

def main_1():
    # the returned object is generator
    generator = some_function()
    print(generator)
    for item in generator:
        print(item)

## 4.1 send method in generator
def double_number(number):
    while True:
        number *= 2
        yield number
        
def main_2():
    generator = double_number(4)
    print(generator.send(None))
    print(generator.__next__())
    print(generator.__next__())
    print(generator.send(8))
    print(generator.send(8))
    print(generator.send(8))
    # the returned valued is affected by send

def double_number_2(number):
    while True:
        number *= 2
        number = yield number
        
def main_3():
    generator = double_number_2(4)
    print(generator.send(None))
    print(generator.send(5))
    print(generator.send(1500))
    print(generator.send(3))
if __name__ == "__main__":
    test_iterator()
    test_ietrable()
    test_iterator_iterable()
    test_iterator_iterable_2()    
    #-------------------
    #main_1()
    #main_2()
    #main_3()
