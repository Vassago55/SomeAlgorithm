# -*- coding:utf-8 -*-
import random


def selection_sort(my_list):
    length = len(my_list)
    if length <= 1:
        return my_list
    for low in range(length - 1):
        min_cursor = low
        for high in range(low+1, length):
            if my_list[min_cursor] <= my_list[high]:
                continue
            elif my_list[min_cursor] > my_list[high]:
                min_cursor = high

        if min_cursor != low:
            my_list[low], my_list[min_cursor] = my_list[min_cursor], my_list[low]

    return my_list


def create_list():
    my_list = [random.randint(0, 1000) for _ in range(1000)]
    print(my_list)
    return my_list


def main():
    my_list = create_list()
    result = selection_sort(my_list)
    print(result)


if __name__ == '__main__':
    main()
