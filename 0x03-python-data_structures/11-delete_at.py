#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return my_list
    for i in range(idx, length):
        my_list[i] = my_list[i + 1]
    del my_list[length]
    return my_list