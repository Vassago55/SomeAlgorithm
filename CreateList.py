# -*- coding:utf-8 -*-
import random


def create_list(start, end, number):
    return [random.randint(start, end) for _ in range(number)]

