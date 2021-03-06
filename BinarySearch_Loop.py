# -*- coding:utf-8 -*-


def binary_search(my_list, target):
    l_cursor = 0
    r_cursor = len(my_list) - 1

    while l_cursor <= r_cursor:
        m_cursor = l_cursor + (r_cursor - l_cursor) // 2

        if target < my_list[m_cursor]:
            r_cursor = m_cursor - 1
        elif target > my_list[m_cursor]:
            l_cursor = m_cursor + 1
        elif target == my_list[m_cursor]:
            return m_cursor

    return l_cursor


def init():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    return my_list


def main(value):
    my_list = init()
    position = binary_search(my_list, value)
    print(position)


if __name__ == '__main__':
    value = input("please in put a number which you want to find:")
    main(int(value))