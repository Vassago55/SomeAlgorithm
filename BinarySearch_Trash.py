# -*- coding:utf-8 -*-

def binary_search(value, my_list):

    length = len(my_list)
    left_cursor = 0
    right_cursor = length - 1
    time = 0

    while True:
        time = time + 1
        if left_cursor is not right_cursor:
            this_cursor = int((left_cursor + right_cursor) / 2)
            if value > my_list[this_cursor]:
                left_cursor = this_cursor + 1
            elif value < my_list[this_cursor]:
                right_cursor = this_cursor - 1
            elif value == my_list[this_cursor]:
                print("{value} in the {position} place.".format(value=value, position=this_cursor))
                break
        else:
            if value is not my_list[left_cursor]:
                print("did not find.")
                break
            else:
                print("{value} in the {position} place.".format(value=value, position=left_cursor))
                break

    print("running {time} times.".format(time=time))


def init():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    return my_list


def main(value):
    my_list = init()
    binary_search(value, my_list)


if __name__ == '__main__':
    value = input("please in put a number which you want to find:")
    main(int(value))