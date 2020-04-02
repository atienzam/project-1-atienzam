# Author: Marc Atienza
# Date: April 1, 2020
# Description: This program takes a list of objects person objects and returns the calculated mean, median and mode of
#               each of the object's ages.

import statistics

class Person:
    def __init__(self, name, age):
        '''
        method that takes name and age of data objects and initializes them
        '''
        self._name = name
        self._age = age

    def get_age(self):
        '''
        method that gets the age of the object
        '''
        return self._age

def basic_stats(person_list):
    '''
    function that creates a list for the ages of the objects and returns
    their calculated mean, median and mode
    '''
    age_list = []
    age_list = [object.get_age() for object in person_list]
    calc_mean = statistics.mean(age_list)
    calc_med = statistics.median(age_list)
    calc_mode = statistics.mode(age_list)

    return calc_mean, calc_med, calc_mode

