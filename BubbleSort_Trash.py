# -*- coding:utf-8 -*-
import random


def bubble_sort(my_list):
    length = len(my_list) - 1
    if length <= 1:
        return my_list
    for _ in range(length):
        flag = 0
        while flag < length:
            if my_list[flag] <= my_list[flag+1]:
                flag = flag + 1
            elif my_list[flag] > my_list[flag+1]:
                my_list[flag], my_list[flag+1] = my_list[flag+1], my_list[flag]

    return my_list


def create_list():
    my_list = [random.randint(0, 1000) for _ in range(1000)]
    print(my_list)
    return my_list


def main():
    my_list = create_list()
    result = bubble_sort(my_list)
    print(result)


if __name__ == '__main__':
    main()
